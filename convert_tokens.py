
def convert_token(token):
    converted = []

    for item in token:
        if item.isdigit():
            item=int(item)
            converted.append(item)
        elif "." in item:
            item=float(item)
            converted.append(item)
        else:
            converted.append(item)

    return converted

