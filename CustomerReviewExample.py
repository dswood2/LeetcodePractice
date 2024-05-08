def searchSuggestions(repository, customerQuery):
    outputs=[]
    loweredRepository=sorted([word.lower() for word in repository])
    for i in range(2, len(customerQuery)+1):
        subQuery = customerQuery[0:i:1].lower()
        matchedWords= []
        for word in loweredRepository:
            if word.startswith(subQuery):
                matchedWords.append(word)
            if len(matchedWords)==3:
                break
        if len(matchedWords) > 0:
            outputs.append(matchedWords)
    return outputs

print(searchSuggestions(["baggage","banner","box","cloths","bags"],"bags"))