from template import *

def main():
    prompt = "Hãy kể cho tôi một sự thật thú vị về Việt Nam."
    for temperature in [0, 0.5, 1, 1.5]:     
        response_text, latency, usage = call_openai(prompt=prompt, temperature=temperature)
        print(f"Temperature: {temperature}")
        print(f"Response: {response_text}")
        print("=" * 50)

if __name__ == "__main__":    
    main()    