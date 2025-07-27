# AI-Chat-Application
Simple AI Chat application with limited and effective frameworks and concepts

A simple yet powerful AI chatbot application built with Gradio and OpenAI's GPT-4 model. This project demonstrates how to create a streaming chat interface that provides real-time AI responses with conversation memory.

**Project Overview**  
This chatbot application consists of two main components:
*  A web-based chat interface built with Gradio
*  A streaming chat engine that connects to OpenAI's API

The application maintains conversation history throughout the session and streams responses in real-time, creating a smooth conversational experience.  

**Project Structure**  
├── stream_chat.py     # OpenAI API integration and streaming logic  
├── ui.py              # Main Gradio interface and application entry point    
├── requirements.txt   # Python dependencies  
└── .env              # Environment variables (you need to create this)  

**File Descriptions**  
**stream_chat.py - AI Chat Engine**  
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

**ui.py - User Interface**  
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

**requirements.txt - Dependencies**  
Contains all necessary Python packages including:  
* gradio==5.38.2 - Web interface framework
* openai==1.75.0 - OpenAI API client
* python-dotenv==0.21.0 - Environment variable management
* Plus additional packages for the broader AI ecosystem

**Installation**  
**1. Clone the repository**  
bash  
git  clone https://github.com/Yegnesh135/AI-Chat-Application.git  
cd ML_project

  
