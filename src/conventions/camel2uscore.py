import re

def camel2uscore(text, allow_spaces=False):
    """
    Description
    ===========
        Converts camel cased word(variable name, JSON key etc.) form to Python compatible underscored form

    Examples
    ========
        + Name -> name
        + name -> name
        + myName -> my_name
        + 788 -> 788
        + year2019 -> year2019
        + isActive -> is_active
        + isTooOld -> is_too_old
        + is___Too___old -> is_too_old
        + is to old -> is_too_old (allow_spaces should be True to allow space separated multi-word text)
        + is-too-old -> is_too_old
    """
    output = ""

    if text.isalnum():
        # Name, name, myName, isTooOld, is__Too___old
        if text.find('_') == -1:
            output = text.lower()
        else:
            # >>> import re
            # >>> 
            # >>> text = "full____name_"
            # >>> output = re.sub(r"_+", '_', text.strip("_")).lower()
            # >>> output
            # 'full_name'
            # >>> 
            # >>> text = "___is__to__old___"
            # >>> output = re.sub(r"_+", '_', text.strip("_")).lower()
            # >>> output
            # 'is_to_old'
            # >>>
            output = re.sub(r"_+", '_', text.strip("_")).lower()
    else:
        # is-too-old, is too old
        pass

    return output


if __name__ == "__main__":
    texts = [
        "Name",
        "name",
        "myName",
        "788",
        "year2019",
        "isActive",
        "isTooOld",
        "is__Too___old",
        "is-too-old"
    ]

    for text in texts:
        print(camel2uscore(text))
