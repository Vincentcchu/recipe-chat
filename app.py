import streamlit as st
import re
from youtube_transcript_api import YouTubeTranscriptApi


def transcript(url):
    video_id = re.search(r'(?<=v=)[^&#]+', url)
    video_id = video_id.group() if video_id else None  # get the matched group if exists
    if not video_id:
        return "Could not extract video ID from URL"
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        return " ".join([i['text'] for i in transcript])
    except:
        return "Could not retrieve transcript for video"


# template = """
# Please carefully review the provided transcript of a cooking 
# video and extract all the necessary information, including the 
# list of ingredients and the step-by-step cooking instructions.
# Transcript: {transcript}\n\n
# Answer: """
# prompt = PromptTemplate(template=template, input_variables=["transcript"])
# llm_chain = LLMChain(prompt=prompt, llm=llm)

# Create the Streamlit app
def main():
    st.title("FALCON LLM Question-Answer App")

    # Get user input
    question = st.text_input("Enter your question")

    # Generate the response
    if st.button("Get Answer"):
        with st.spinner("Generating Answer..."):
            response = transcript(question)
        st.success(response)

if __name__ == "__main__":
    main()