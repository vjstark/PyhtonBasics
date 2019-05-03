import requests
paper_url = 'https://images.unsplash.com/photo-1527685816164-fa0d282cd89a?ixlib=rb-0.3.5&ixid=eyJhcHBfaWQiOjEyMDd9&s=5966265b011e0dc88159651005445596&auto=format&fit=crop&w=1848&q=80'
r=requests.get(paper_url)
print(r)
with open('paper.jpg','wb') as f:
	f.write(r.content)