import pprint
import time

import scrapy
from ..items import ExtraccionItem


class WsSorianaSpider(scrapy.Spider):
    name = "ws_soriana"
    allowed_domains = ["soriana.com"]
    start_urls = ["https://www.soriana.com/on/demandware.store/Sites-Soriana-Site/default/Page-RenderHeaderMenu"]
    complete_url = f"https://{allowed_domains[0]}"
    item = ExtraccionItem()

    def start_requests(self):

        # Nos podemos saltar a esta pagina evitando el indez, ya que esta en especifico
        # Nos despliega la informacion que requerimos

        url = "https://www.soriana.com/on/demandware.store/Sites-Soriana-Site/default/Page-RenderHeaderMenu"

        # Este payload nos pide un tamaño de pantalla para poder redesplegar el menu
        # Puede ser un dato directo o aleatorio

        payload = {"wScreen": "1680"}

        # Encabezados de la peticion que se pueden utilizar para el llamado
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/111.0',
            'Accept': '*/*',
            'Accept-Language': 'es-MX,es;q=0.8,en-US;q=0.5,en;q=0.3',
            'Accept-Encoding': 'gzip, deflate, br',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'X-Requested-With': 'XMLHttpRequest',
            'X-KL-saas-Ajax-Request': 'Ajax_Request',
            'Origin': 'https://www.soriana.com',
            'Connection': 'keep-alive',
            'Referer': 'https://www.soriana.com/',
            'Cookie': 'dwac_f1e552945f65c8b8b0264c1a64=58xB0KmMnHxW58Ac_6TQ8qV7a0DoowwdyMs%3D|dw-only|||MXN|false|America%2FMexico%5FCity|true; cqcid=abmxAzAn88FwIWPSR7AgFoE6ZC; cquid=||; dwanonymous_ad95070cfe256984fa6223b8e5b1c401=abmxAzAn88FwIWPSR7AgFoE6ZC; sid=58xB0KmMnHxW58Ac_6TQ8qV7a0DoowwdyMs; __cq_dnt=0; dw_dnt=0; dwsid=-dfftgMYWtCq_ROCWN9UwLtg9SZCN8qxNNFDBZy5BViMYwpkwCUiC2lGZDLCF3UEBRNC3rPZ0h-pfuwr33JEQQ==; _abck=B6A5B387A96FEAF87F46C557117753E6~0~YAAQFJUgF55ufuaGAQAAdFgF6QkZLEeieeXYK+I5YCfZvQo8UcafVHpjcL/yQOhn6lJFjXfpiioKWoF1s6S2imtWQVxjEASdIXEiT+5lp4WAhZaGvYgQwINhqLiOB6iPWtehNgrv2kMkChdorKwfvbxywziEiBmx3IsI3uGHsEd7Yq9VgOPS2BY28imiMQRkm9SvyZmS6eUS0sJHU93djelLl58tNmZ5XILXkO6NkCuo7jhgVKNn2pt2tYdPAKQiuzRU9PJUrn8zsCENDMEibwdwMDpl6Yl/DHgJu6ukG3FyogGhslfbErxx0RPDT0YGNY682VwBiBy6oRMYQcr3l9lSmMERiY5ao+LYXsv0bCO6Hxe0pYwKg/YyuO/9kM+S9VZYCVCnzWA4v2HBZ7oPqtx8WP6f7KIz9z4=~-1~||-1||~-1; bm_sz=6C38B8C6D56995BA59BEBA40CD81BE5C~YAAQFJUgF3ZmfuaGAQAAhgIF6ROFxizI0APQfFgoA1UPK7jW1XxQsbwdp87xTL30pPTTkL78ahnwXPbNe6dZym6PG1qEYZFnKRUmDmtJkossLOgNK2eGxvHsqVdforin6vFFwGeZvYa1iesE4eE4++g37PQbUdKkkl9lVzieMbILdX6Q7v53GrdzeTNJoH5w1pz+DeyvRdYqLPVcaaJ3HVstDZmiGEkLnPKmAEr7A6elljC7o5UpDuAkOrYDU+ZAnnP0ZkmBxzbIrK6F30sW3uIx8QUMEiqxY8SEE0IeR9fOgI7N~4405046~3421237; PIM-SESSION-ID=rf2iOl9bLID0IgwW; BVBRANDID=813049ec-73cc-4e56-a9c8-185c9ab0b1fd; RT="z=1&dm=soriana.com&si=bafbd9c2-d41f-4d06-9af6-7b363b8aa650&ss=lfatg784&sl=3&tt=hw7&bcn=%2F%2F17de4c13.akstat.io%2F&ld=jk9r"; _ga_LZ2D37D7GQ=GS1.1.1678953312.3.1.1678954217.58.0.0; _ga=GA1.2.440209077.1678946683; _gcl_au=1.1.1778932579.1678946683; __cq_uuid=abmxAzAn88FwIWPSR7AgFoE6ZC; __cq_seg=0~0.00!1~0.00!2~0.00!3~0.00!4~0.00!5~0.00!6~0.00!7~0.00!8~0.00!9~0.00; __rtbh.lid=%7B%22eventType%22%3A%22lid%22%2C%22id%22%3A%22JDAJBckbK2u9fvrRla6w%22%7D; _gid=GA1.2.1497518819.1678946686; _pin_unauth=dWlkPVpUbG1ZMkV3T1RjdFpHVmhOQzAwTkdGbUxXRTFOVE10TWpWbU4yUTJOV1EwWWpJdw; _tt_enable_cookie=1; _ttp=qjolX-tS1v6T3nciunCNfJEa1Mu; _hjSessionUser_464447=eyJpZCI6IjU3MGM5ZjM1LTI1YmYtNTZlZC05ZTcyLThiNTUwOWRiNTZlZSIsImNyZWF0ZWQiOjE2Nzg5NDY2ODcwMzcsImV4aXN0aW5nIjp0cnVlfQ==; _hjIncludedInSessionSample_464447=1; _hjIncludedInPageviewSample=1; _fbp=fb.1.1678946689789.228919272; BVBRANDSID=6404a5af-fa2e-4ede-bfa8-b153a41009d8; _hjSession_464447=eyJpZCI6IjM4ODYxOTYyLTVmNDItNGFmYi05ODI3LTAxZDAwN2UzOGY3OSIsImNyZWF0ZWQiOjE2Nzg5NTMzMTM1MjEsImluU2FtcGxlIjp0cnVlfQ==; _hjAbsoluteSessionInProgress=0; ak_bmsc=7F0AC81852B2A4B694B86A6D9065F940~000000000000000000000000000000~YAAQxThjaEiI88CGAQAAMEF46RO5Y9GBbtHI0ysqfE6lI93TUU+cu4c2Nj0TPviuXBuso2fdrkWScw0TIonwecqCE46TodXRk64bDl+H+n11QIyrqh6qQ7lIBdvsnI5GCSNbvKyLMKvk2iKfOKUXp6xbOzj8lXGDLEes3NE5BKv1z1cFjDuDXFv3aCfChYba/otsftCrslDl/Rkp/oGn0TNXECaBx26EtSpdk9vofLloEIDfBEnX5dbdtKdIF1DkKBmK3u65VHlCN+QRlz+zTHmP8A+9LotoqWRooSMJ+2zyFWUvoNcRcbzqU6GV0ITMgxJ68RViY3aH8WnyaAjWopPzQOvFzwWXGyCLGzYfty5OpSSUfeSFp/pnF5cQLTWGA1LWRqPYySOJb8G8AfFhR7FXPaVPyDAXGwcfyw==; bm_mi=952B57ED5354602DF7162673AD6533AB~YAAQxThjaCKI88CGAQAA2zV46RNshu61I81MscRCOEz0wO1dUbgrGw7rY6O+0sqCbMt6+up343dfGpwpRw99FysVSvObS84NQsbF2cIxs2hvJbPZUlvjJ/OlVknYkSiX3jUmlJoosQocA89JnAOQ3bHNPfh68F0zTXy6kM2xjD0mXCCo8adnbx2LZ0EHY1TIih6QA+05iWT/I+fXO2Jytt5qSnSeiVx+br1Mejj+qXgREBCvLHwmJyu0O9/jVxMzlwLNXP/bvkVejoFeH0mp2vDUu1YEJZERLyXpXzzWThvRGX/Ln+q3lgY+jGSswQ==~1; bm_sv=9E0A7C41B61CF627629182665647B630~YAAQxThjaEmI88CGAQAAMEF46ROQRCfvCwYTVEfPfkCUzHftODBuMgjZvp/cM0PQxWK4xFNI7S1Ma3pz6a5z9mArzboYrrMqkjUqmUWqh6v5QsFQDCCHLqX9uPfe+vNYRxC+j40ftKA0C+oZp7vtdQH/qYy99cJjFMz40NCgyzC95QpXRV2W+p/7uTEd8c7yiyZdaNaS+OdP121tjcLW64GTNr/9dfPrm/f9Sc3OIPu0MHcaMfVtLj5h4F0cJ5pFuw==~1; _abck=B6A5B387A96FEAF87F46C557117753E6~-1~YAAQxThjaGGN88CGAQAApE166QkEVoLquW/hHRF8dhpNOzXXaVBxFE1Kw3SvfzfAZJi8nPVH3hIh8xkd8ufeInHY2mO+xkLFK/Ugx3vIhRIqNRWwDlphwcNiwDJ4yKTwe6mw/7w9dyH4ah1mzrZjP4L2ldKt4NrEj/DodXgTdObZYim+Db9DQWmvL1mTTDHVOrckbodBPZx2GRaLdZU+jDfYfst10fyYUszeNYI9h1AKK9v0mXZ/jeqdwmTHfBzXEJENeRVIBaXU3KWIX0A7iUdDylTbmHLnH9qnYaz1ClHxnXxY6mwhVZrPpDZni6LHbXG5xbaJ6UBZIVwKwpB7soYKYCERKTXFWzhp+4SNNA4BckJ3mdn3xhynJI+1L8/4OICP3UxXeyjrGJML7ZnIWVRp/ZNl5ZKXtSg=~0~-1~-1; bm_mi=755D75585B14D9EFF259833617319EFF~YAAQFJUgF7N9guaGAQAAzVBE6RMFQcvycUjLw71V3O6jCB0TxPFGVmKzTTD4w0sh6hKhHHHMtcEpw7QwovpESKV8jCueV80xvePGAKTfAnY7J2XO+9nPJd4qAfn10ak4/34mKV9S8k6ffraljPz5KmHCcm21JPuD4VIDPtli5iR+FIBsoRhxh8E7ce3tmjhzPl3ilBTnyQKL/ub+2ZrdZ5UnS3JY+9AHyrl8QPRmg0qDtjlw34TrDncDkkLEMKw69c8L9CPxL0yItJ+r86OQO0dYu1mXgZmP+/2ReYpoj4AYT5KwwofXw1Oe6+F3ZQE=~1; bm_sv=9E0A7C41B61CF627629182665647B630~YAAQxThjaGKN88CGAQAApE166RPba/u7fQalbQYiyCv4Rr9UluUViVP15rNgqujlRLzMWPjjBNDl2UNzN3dzWqgNCJSmzEuzwArNimgfpn9ryfQzlN56aCt5yw/YZSvpakolFky0pC30eaP1NhortCNrR9b4a660OtmjFsBEuSs3Zin+DZXRbIZ3bMCojyFeAjgJnUF7PzJRWkVJR8kPPLWm1fF9nUQSYcwAHvoDmsgMAkOeBHcblHpqG/9fxhOO3g==~1; bm_sz=3A6D5FF15AA9586F993DF298D74AB842~YAAQFJUgF7cTf+aGAQAAHcwM6RPY/dGLWDPqAzmX8NwtO13Bx4mHFE5/LbEZEI5fGMpVXbTF+uiqDfUaXGEJ/oc4TEef3c7PtfsAEPpAuLIIfhA9fZi9mFYmMzJq8rQbwP01Der8SyztyQryZLbSduTglKvb2KKDkAaE1n1uiWfDHkjd2PxDD/roYFRaYkh7UHiCspfrNYzWVkW4uTLWBLGxcB8C14Ndko+KfS3h0C5Ec4BO5NCsf8pTFhJR9CvG03mrAdsawngfBj4PMJyoOg8QqWb+WSEcrgs2NNdkc1bubHsy~3228725~3622196; __cq_dnt=0; cqcid=ab4NrAqJ6xRa0nReAaMnMeQUlD; cquid=||; dw_dnt=0; dwac_f1e552945f65c8b8b0264c1a64=1ow97Y5ckapQow_O66sOkhVUeE8qM9oObvI%3D|dw-only|||MXN|false|America%2FMexico%5FCity|true; dwanonymous_ad95070cfe256984fa6223b8e5b1c401=ab4NrAqJ6xRa0nReAaMnMeQUlD; dwsid=s31_4V__R8TXu7GW2gZbhnClOkP7kAxg6erSPOA6qLtXkaKnEvD5pgMG366DYokY867_kHuWCDASO_R6FLeJJg==; sid=1ow97Y5ckapQow_O66sOkhVUeE8qM9oObvI',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'TE': 'trailers'
        }

        # Enviamos el flujo a una fase 2
        yield scrapy.FormRequest(
            url=url,
            formdata=payload,
            headers=headers,
            callback=self.parse
        )

    def parse(self, response):
        if response.status == 200:

            # En base a XPATH obtenemos los datos necesarios directos del HTML
            container_despensa = response.xpath('//div[@id="subcat-despensa"]//div[@class="subcat-list row d-flex"]')

            self.item['department'] = (response.xpath('//a[contains(text(), "espensa")]/text()').get()).strip('\n')
            self.item['url'] = response.xpath('//a[contains(text(), "espensa")]/@href').get()
            self.item['categories'] = []

            # Recorremos el contenedor del bloque que nos interesa
            for category in container_despensa:
                subcontainer_despensas = category.xpath('.//div[@class="one-third"]')

                # Recorremos las subcategorias
                for subcategory in subcontainer_despensas:

                    subcategory_name = (subcategory.xpath('.//div[@class="cat-title"]/a/text()').get()).strip('\n')
                    subcategory_url = f"""{self.complete_url}{subcategory.xpath('.//div[@class="cat-title"]/a/@href').get()}"""

                    container_product = subcategory.xpath('.//ul//li/a')

                    subcategories = []

                    # Recorremos cada producto
                    for product in container_product:

                        product_name = product.xpath('./text()').get().strip('\n')
                        product_url = f"""{self.complete_url}{product.xpath('./@href').get()}"""

                        subcategories.append({'name' : product_name, 'url' : product_url})

                    # Almacenamos la informacion correspondiente dentro de su item
                    self.item['categories'].append({'name' : subcategory_name, 'url' : subcategory_url, 'subcategories' : subcategories})

            pprint.pprint(self.item)
            # Retornamos el JSON completo
            return self.item