s = input()

if s.count('@') != 1:
    print('no')
else:
    local, domain = s.split('@')
    if len(local) not in (2, 3, 4):
        print('no')
    elif not local.isalpha() or not local.islower():
        print('no')
    elif domain != 'odoo.com':
        print('no')
    else:
        print('yes')
