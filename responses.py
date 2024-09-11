from difflib import get_close_matches
import json

def get_best_match(user_question: str, questions: dict) -> str | None:
    questions: list[str] = [q for q in questions]
    matches: list = get_close_matches(user_question, questions, n=1, cutoff=0.3)

    if matches:
        return matches[0]
    

def get_response(message: str, knowledge: dict) -> str:
    best_match: str | None = get_best_match(message, knowledge)

    if answer := knowledge.get(best_match):
        return answer
    else:
        return "I don\'t understand... Could you perhaps try rephrasing that with shorter words? I am not trained well enough. I'll leave this one to the admins!"
    

def load_knowledge(file: str) -> dict:
    with open(file, 'r') as f:
        return json.load(f)
    

if __name__ == '__main__':
    test_knowledge: dict = load_knowledge('knowledge.json')
    test_response: str = get_response('Hey there', knowledge=test_knowledge)
    print(test_response)
