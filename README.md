# AI-Chat-Application
**Simple AI Chat application with limited and effective frameworks and concepts**

<img width="1550" height="883" alt="Screenshot 2025-07-27 161650" src="https://github.com/user-attachments/assets/a916bbc0-009a-49ff-a52d-246916a5eaea" />


A simple yet powerful AI chatbot application built with Gradio and OpenAI's GPT-4 model. This project demonstrates how to create a streaming chat interface that provides real-time AI responses with conversation memory.

**📋 Project Overview:**  
This chatbot application consists of two main components:
*  A web-based chat interface built with Gradio
*  A streaming chat engine that connects to OpenAI's API

The application maintains conversation history throughout the session and streams responses in real-time, creating a smooth conversational experience.  

**Project Structure:**  
├── stream_chat.py     # OpenAI API integration and streaming logic  
├── ui.py              # Main Gradio interface and application entry point    
├── requirements.txt   # Python dependencies  
└── .env              # Environment variables (you need to create this)  

**📁 File Descriptions:**  
**stream_chat.py - AI Chat Engine:**  
This file handles all AI-related functionality including:  
* OpenAI API integration using the official Python SDK  
* Conversation history management  
* Real-time response streaming  
* System prompt configuration for the AI assistant

**Key Features:**  
* Streaming responses for real-time chat experience
* Conversation memory that maintains context
* Configurable AI personality through system prompts
* Error handling for API communications

**AI Configuration:**  
* Model: GPT-4.1 (2025-04-14)
* Streaming: Enabled for real-time responses
* System Role: Technical assistant focused on clear, actionable guidance

**ui.py - User Interface:**  
This file contains the main application interface built with Gradio. It:  
* Creates a chat interface using gradio.ChatInterface
* Manages conversation state across the session
* Provides a "Clear State" button to reset conversations
* Launches the web application with sharing enabled

**Key Features:**  
* Clean, responsive chat interface
* Real-time message display
* Conversation state management
* Easy conversation reset functionality

**requirements.txt - Dependencies:**  
Contains all necessary Python packages including:  
* gradio==5.38.2 - Web interface framework
* openai==1.75.0 - OpenAI API client
* python-dotenv==0.21.0 - Environment variable management
* Plus additional packages for the broader AI ecosystem

**Installation:**  
**1. Clone the repository:**  
```bash  
git  clone https://github.com/Yegnesh135/AI-Chat-Application.git  
cd ML_project
```

**2. Install dependencies:**
```bash
pip install -r requirements.txt  
```

**3.Set up environment variables:**  
Create a .env file in the project root:
```
OPENAI_API_KEY=your_openai_api_key_here
```

**4. Run the application:**  
```
python ui.py
```

    
The application will start and display:  
* Local URL (usually http://localhost:7860)
* Public sharing URL for remote access

**💬 How It Works:**  
**Conversation Flow:**  
1. User enters a message in the chat interface
2. The message is sent to stream_chat() function
3. If it's a new conversation, a system message is added to establish the AI's role
4. The user's message is added to the conversation history
5. The complete conversation history is sent to OpenAI's API
6. The AI response is streamed back in real-time chunks
7. Each chunk is yielded immediately to update the UI
8. The complete response is added to conversation history for context

**Streaming Implementation:**  
The streaming feature works by:  
1. Setting stream=True in the OpenAI API call
2. Processing response chunks as they arrive
3. Building the complete response incrementally
4. Yielding the growing response for real-time UI updates
```
full_response = ""
for chunk in response:
    if chunk.choices[0].delta.content:
        chunk_content = chunk.choices[0].delta.content
        full_response += chunk_content
        yield full_response  # Real-time update
```

**⚙️ Configuration:**  
**AI Behavior:**  
The AI assistant is configured with a system prompt that makes it:  
* Focus on technical assistance
* Provide clear, understandable explanations
* Offer actionable advice that users can implement
* Maintain a helpful and professional tone

You can modify the system message in stream_chat.py to change the AI's personality or expertise focus.  

**Interface Customization:**  
The Gradio interface can be customized by modifying ui.py:  
* Adjust chatbot height: gradio.Chatbot(height=500)
* Change title and description in gradio.ChatInterface
* Add additional UI components like sliders or text inputs

**🛠️ Technical Features:**  
**Real-Time Streaming:**  
* Immediate response delivery as the AI generates text
* No waiting for complete responses before display
* Smooth, natural conversation flow

**Conversation Memory:**  
* Complete conversation history maintained during the session
* Context preservation for multi-turn discussions
* Easy conversation reset with "Clear State" button

**Error Handling:**  
* Graceful handling of API errors
* Proper exception management in streaming responses
* User-friendly error messages

**🔧 Customization Options:**  
**Changing AI Model:**  
To use a different OpenAI model, modify the model parameter in stream_chat.py:  
```
response = openai.chat.completions.create(
    model="gpt-3.5-turbo",  # or another model
    messages=conversation_history,
    stream=True
)
```
**Adjusting Response Behavior:**  
Add parameters to control AI responses:  
```
response = openai.chat.completions.create(
    model="gpt-4.1-2025-04-14",
    messages=conversation_history,
    stream=True,
    temperature=0.7,  # Creativity level (0-1)
    max_tokens=500,   # Response length limit
)
```
**UI Modifications:**  
Customize the interface in ui.py:  
```
chat_interface = gradio.ChatInterface(
    stream_chat,
    type="messages",
    chatbot=gradio.Chatbot(height=600),  # Adjust height
    title="My Custom AI Assistant",      # Change title
    description="Your personalized description"
)
```
**🔄 Future Enhancements**  
This basic implementation can be extended with:  
* Multiple AI models support
* Conversation history persistence
* User authentication and sessions
* File upload capabilities
* Custom knowledge base integration
* Response export functionality

**🤝 Contributing**  
Feel free to submit issues, fork the repository, and create pull requests for any improvements.

