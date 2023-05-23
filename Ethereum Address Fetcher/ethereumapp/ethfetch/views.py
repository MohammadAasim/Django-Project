from django.shortcuts import render
import requests

def home(request):
    return render(request, 'ethfetch/home.html')

def fetch(request):
    if request.method == 'POST':
        address = request.POST['address']
        api_key = '613EWC49SFB4C5TEHRY4YTXKPTVYM8J8DK'  # Replace with your Etherscan API key
        
        balance_url = f'https://api.etherscan.io/api?module=account&action=balance&address={address}&apikey={api_key}'
        transaction_url = f'https://api.etherscan.io/api?module=account&action=txlist&address={address}&apikey={api_key}'

        balance_response = requests.get(balance_url)
        transaction_response = requests.get(transaction_url)

        balance = balance_response.json()['result']
        transactions = transaction_response.json()['result'][:5]

        context = {
            'address': address,
            'balance': balance,
            'transactions': transactions,
        }

        return render(request, 'ethfetch/home.html', context)

    return render(request, 'ethfetch/home.html')
