def filtrate(string, lower=True, split_=True, split_basis=" ", filt=True, filter_basis=" "):
    # Lowercasing the string if lower is True
    try:
        if lower:
            string = string.lower()

        # Filtering the string based on filter_basis if filt is True
        if filt:
            # Trim extra spaces from start, end, and middle of the string
            string = ' '.join(string.split())

        # Splitting the string into a list of substrings based on split_basis if split_ is True
        if split_:
            string_list = string.split(split_basis)
            return string_list
        else:
            return string
    except:
        return ""
if __name__== "__main__":
    
    input_string = "   Hello  wae World   "
    result = filtrate(input_string, lower=True, split_=True, split_basis=" ", filt=True, filter_basis=" ")
    print(result)