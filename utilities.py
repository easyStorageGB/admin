import requests
from tenacity import retry, wait_random_exponential, stop_after_attempt

@retry(wait=wait_random_exponential(multiplier=1, max=40), stop=stop_after_attempt(3))
def aichat(messages, client, model):
    try:
        # client = openai.OpenAI(api_key = openai_api_key)
        response = client.chat.completions.create(
            messages=messages,
            model=model,
            stream=True,
        )
        return response
    except Exception as e:
        print("Unable to generate ChatCompletion response")
        print(f"Exception: {e}")
        return e

def get_item_sizes():
    url = "https://hypech.com/StoreSpark/easystorage/item_sizes.json"
    response = requests.get(url)     
    if response.status_code == 200:  
        data = response.text                  
        return data
    else:
        print(f"The store is closed：{response.status_code}")    

def get_packing_material_charges():
    url = "https://hypech.com/StoreSpark/easystorage/packing_material_charges.json"
    response = requests.get(url)     
    if response.status_code == 200:  
        data = response.text                  
        return data
    else:
        print(f"The store is closed：{response.status_code}")    

def get_pod_container_prices():
    url = "https://hypech.com/StoreSpark/easystorage/pod_container_prices.json"
    response = requests.get(url)     
    if response.status_code == 200:  
        data = response.text                  
        return data
    else:
        print(f"The store is closed：{response.status_code}")    

def get_embedding(text, model="text-embedding-3-small"):
   text = text.replace("\n", " ")
#    return client.embeddings.create(input = [text], model=model).data[0].embedding

# text = "test embedding"
# embeddings = get_embedding(text)