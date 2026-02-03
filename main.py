from ai_agent import create_ollama_ai_provider

def extract_memories(prompt: str, response: str, ai_provider):
    memory_prompt = f"""
        You are a memory extractor. Convert the following conversation into a list of short, self-contained factual sentences. 

        Rules:
        - Each fact must be one complete sentence. 
        - Each sentence must be self-contained: avoid pronouns without context. 

        Conversation:

        Prompt:
        {prompt}

        Response:
        {response}

        Return only the sentences, one per line.
        """
    raw = ai_provider.generate(memory_prompt)
    sentences = [s.strip().rstrip(".") + "." for s in raw.split("\n") if s.strip()]
    # remove duplicates
    sentences = list(dict.fromkeys(sentences))
    return sentences

def main():
    
    ai_provider = create_ollama_ai_provider()

    prompt_text = """Tell me the story of US"""
    try:
        print("Prompt:\n", prompt_text)
        response = ai_provider.generate(prompt_text)
        print("Response:\n", response)
        information = extract_memories(prompt_text, response, ai_provider)
        print("Response for memory:\n", information)
    except Exception as e:
        print(f"Error during AI generation: {e}")


if __name__ == "__main__":
    main()