const API_BASE = 'http://localhost:5000';

let chatbotOpen = false;
let conversationHistory = [];

function createChatbotWidget() {
  const widget = document.createElement('div');
  widget.id = 'chatbot-widget';
  widget.innerHTML = `
    <div class="chatbot-button" onclick="toggleChatbot()">
      <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
        <path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"></path>
      </svg>
    </div>
    <div class="chatbot-window" id="chatbot-window">
      <div class="chatbot-header">
        <div class="chatbot-title">
          <span>🌱 Wellness Assistant</span>
        </div>
        <button class="chatbot-close" onclick="toggleChatbot()">×</button>
      </div>
      <div class="chatbot-messages" id="chatbot-messages">
        <div class="message bot">
          <div class="message-content">
            Hello! I'm your wellness assistant. I can help you with stress management, mental wellness tips, and answer questions about the Ikigai platform. How can I help you today?
          </div>
        </div>
      </div>
      <div class="chatbot-input-area">
        <select id="chatbot-mode" class="chatbot-mode-select">
          <option value="listener">Listener</option>
          <option value="motivator">Motivator</option>
          <option value="advisor">Advisor</option>
        </select>
        <input type="text" id="chatbot-input" placeholder="Type your message..." onkeypress="handleChatbotKeyPress(event)">
        <button onclick="sendChatbotMessage()" class="chatbot-send-btn">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <line x1="22" y1="2" x2="11" y2="13"></line>
            <polygon points="22 2 15 22 11 13 2 9 22 2"></polygon>
          </svg>
        </button>
      </div>
    </div>
  `;
  document.body.appendChild(widget);
}

function toggleChatbot() {
  chatbotOpen = !chatbotOpen;
  const window = document.getElementById('chatbot-window');
  if (chatbotOpen) {
    window.style.display = 'flex';
    document.getElementById('chatbot-input').focus();
  } else {
    window.style.display = 'none';
  }
}

function handleChatbotKeyPress(event) {
  if (event.key === 'Enter') {
    sendChatbotMessage();
  }
}

async function sendChatbotMessage() {
  const input = document.getElementById('chatbot-input');
  const message = input.value.trim();
  
  if (!message) return;
  
  const mode = document.getElementById('chatbot-mode').value;
  const messagesDiv = document.getElementById('chatbot-messages');
  
  addChatbotMessage(message, true);
  input.value = '';
  
  const loadingMsg = addChatbotMessage('Thinking...', false, true);
  
  try {
    const response = await fetch(`${API_BASE}/chatbot`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ 
        message, 
        mode,
        conversation_history: conversationHistory.slice(-5)
      })
    });
    
    const result = await response.json();
    loadingMsg.remove();
    
    if (result.status === 'success') {
      addChatbotMessage(result.response, false);
      
      conversationHistory.push(
        { role: 'user', content: message },
        { role: 'assistant', content: result.response }
      );
      
      if (result.crisis_detected && result.resources) {
        addChatbotMessage(`⚠️ Resources: ${result.resources.join(', ')}`, false);
      }
    } else {
      addChatbotMessage(`Error: ${result.message}`, false);
    }
  } catch (error) {
    loadingMsg.remove();
    addChatbotMessage('Unable to connect to server. Make sure Flask is running on port 5000.', false);
  }
}

function addChatbotMessage(text, isUser, isLoading = false) {
  const messagesDiv = document.getElementById('chatbot-messages');
  const messageDiv = document.createElement('div');
  messageDiv.className = `message ${isUser ? 'user' : 'bot'}`;
  if (isLoading) messageDiv.classList.add('loading');
  
  const contentDiv = document.createElement('div');
  contentDiv.className = 'message-content';
  contentDiv.textContent = text;
  messageDiv.appendChild(contentDiv);
  
  messagesDiv.appendChild(messageDiv);
  messagesDiv.scrollTop = messagesDiv.scrollHeight;
  
  return messageDiv;
}

if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', createChatbotWidget);
} else {
  createChatbotWidget();
}
