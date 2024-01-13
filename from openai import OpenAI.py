from openai import OpenAI
import streamlit as st

# Create OpenAI client
clt = OpenAI(api_key="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")

# Function to generate article
def generate_article(topic_notes):
   with st.spinner("Generating Article..."):
       response = clt.chat.completions.create(
           model="gpt-3.5-turbo",
           messages=[{'role': 'user', 'content': f"I want you to write short literature review on topic notes: {topic_notes}"}]
       )
       description = response.choices[0].message.content
       return description

# Main function
def main():
   st.title("Article Writer")

   notes = st.text_area("Enter Topic Information:")

   if st.button("Generate Article"):
       generated_article = generate_article(notes)
       st.subheader("Generated Writeup:")
       st.write(generated_article)

# Run the app
if __name__ == "__main__":
   main()