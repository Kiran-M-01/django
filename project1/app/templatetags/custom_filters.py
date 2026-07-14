from django import template

register = template.Library()

@register.filter
def vowels(value):
    out = ''
    for i in value:
        if i in 'aeiouAEIOU':
            out += i
    return out

@register.filter
def freq(value):
    out = {}
    for i in value:
        out[i] = value.count(i)
    return out


@register.filter
def divisible(value, args):
    return value % args == 0


@register.filter
def prime(value, args):
    for i in range(value,args+1):
        if i == 0 or i == 1:
            return False
        for j in range(2,i):
            if i%j == 0:
                return False
    return True

# ASSIGNMENT
@register.filter
def multiply(value, arg):
    return value * int(arg)




@register.filter
def add_num(value, arg):
    return value + int(arg)



@register.filter
def guess_num(value, arg):
    return value == arg



# imp  

@register.filter
def is_vowel(value):
    if value in 'aeiouAEIOU':
        return f"{value} is vowel"
    return f"{value} is not vowel"
    

    