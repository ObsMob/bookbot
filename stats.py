def word_count(file_contents):
    word_list = file_contents.split()
    return len(word_list)

def character_dict(file_contents):
    characters = {}
    lowercased = file_contents.lower()
    for lowercase in lowercased:
        if lowercase in characters:
            characters[f"{lowercase}"] += 1
        else:
            characters[f"{lowercase}"] = 1
    return characters

def dict_sort(character_dict):
    def sort_value(sorted):
        return sorted["value"]
    sorted = []
    for character in character_dict:
        sorted.append({"character": character, "value": character_dict[character]})
    sorted.sort(reverse=True, key=sort_value)
    return sorted