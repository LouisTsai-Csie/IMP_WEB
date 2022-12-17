from phe import paillier

def GOT_GPT_calc(encrypted_number_list, public_key):
    _encrypted_number_list = [paillier.EncryptedNumber(public_key, x, 0) for x in encrypted_number_list]
    GOT = _encrypted_number_list[0]
    GPT = _encrypted_number_list[1]
    neg_GOT = GOT.__mul__(-1)
    neg_GPT = GPT.__mul__(-1)

    neg_GPT_difference = GOT.__add__(neg_GPT)

    GOT_difference_with_normal = GOT.__add__(-40)
    GOT_difference_with_upper  = neg_GOT.__add__(200)

    neg_GOT_difference = GPT.__add__(neg_GOT)

    GPT_difference_with_normal = GPT.__add__(-40)
    GPT_difference_with_upper  = neg_GPT.__add__(200)

    GOT_exceed = GOT.__add__(-1000)

    GPT_exceed = GPT.__add__(-1000)

    result_value = [neg_GPT_difference, GOT_difference_with_normal, GOT_difference_with_upper, neg_GOT_difference, GPT_difference_with_normal, GPT_difference_with_upper, GOT_exceed, GPT_exceed]
    return result_value
