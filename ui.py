from stream_chat import stream_chat
import gradio

def main():
    
    with gradio.Blocks() as demo:
        conversation_state=gradio.State([])

        chat_interface=gradio.ChatInterface(
            stream_chat,
            type="messages",
            chatbot=gradio.Chatbot(height=500),
            title="Yegnesh AI Chatbot",
            description="An AI assistant to help you with your queries.",
        )

        def clear_conversation():
            return [],[]
        
        clear_btn=gradio.Button("Clear State")
        clear_btn.click(
            clear_conversation,
            outputs=[conversation_state, chat_interface.chatbot]
        )
    
    demo.launch(share=True)


if __name__ == "__main__":
    print(50*"-")
    main()