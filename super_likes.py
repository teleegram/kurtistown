import uuid
import json
import time
import requests
import time
import argparse


def more_likes(args):
	counter = 0
	while True and counter < args.max_likes:
		email = f"{uuid.uuid4().hex[:10]}@{uuid.uuid4().hex[:10]}.com"
		username = f"{uuid.uuid4().hex[:10]}"
		try:
			with requests.session() as sess:
				res1 = sess.post('https://crud.api-world.co/api/v1/users/', json = {"email":email,"username":username,"password":"Simpiser243#","avatar":{"avatarAttributes":{"body":"924d8113-f0ed-46a9-b9bd-9f4f736fb8e4","eyes":"9027ee46-f304-4733-bd96-badc559cb0a8","eyebrowColor":"#303336","hairColor":"#303336","skinTone":"5d2471cd-6469-4cbb-b331-163bd3d006ec"},"morphTargets":{"gender":"male"},"wearables":{"bottom":"8d8f700b-a05c-48cb-be18-d16195986da7","hair":"fb365c15-bd9a-45dc-ad7f-a40495da77a0","shoes":"db6656ae-c2b4-4f74-9efd-67774ba90d8c","top":"039d5bdb-f052-47fd-b54d-e2facacf1a36"}},"avatarImage":"https://api.urlbox.io/v1/MA2A7h8lgSs9FAok/488219e18b1b2afe15537316375685c8012192ee/png?width=400&height=400&url=https%3A%2F%2Fwebviews.mpreview.app%2Fheadshot%2F_body--924d8113-f0ed-46a9-b9bd-9f4f736fb8e4_eyes--9027ee46-f304-4733-bd96-badc559cb0a8_eyebrowColor--303336_hairColor--303336_skinTone--5d2471cd-6469-4cbb-b331-163bd3d006ec_hair--fb365c15-bd9a-45dc-ad7f-a40495da77a0_top--039d5bdb-f052-47fd-b54d-e2facacf1a36_gender--male&wait_for=%23urlbox-flag&gpu=true&fail_if_selector_missing=true","timezone":"Europe/London","worldId":"47580924-beb3-41ee-ac5c-8555fc7bdeb5","worldsOnboarding":True,"shareEmail":False,"autoFollowId":"16a7d4c9-4765-4dd6-ba72-bc7c93533911","captchaToken":"03AAYGu2RN5eaIhM6_fR_RRtsP1vn6ArotiFcDIdV5_PSfPfLsShQX3JSVw7Strvro_852__am1J50aGB7Nh7uGkwn4mRB9Wa2eHzn4TtNX8PEzoG7Dr1gs4DEmTsizHekzmHYvZychAVgv79K82ivnjkUfXxMfcKsM_yX4AadhcWG1VzWVVkNm6LT1OxB6z1xoR42RkgZEG1HHsyIbFljhgxREkFbpsnx2YzWehZ7HoM5_ObBaFSMjpGHJzeRFngDBgPWT8TIGel-BDiOtR8XeZYbwX6Qc9Ch8Poghf1ld8G4sSR8Vc9bCBUYeaQa0pWk7GnQo0WExRDEVgYxUnbJqApoqC_hJcudc61kNLN-RoJJVGdkuH5r2Ug5SFS7Wl8lyPl9SOo6zXbklaAz4iblHynoSROB3ba09cPtLLT1KFsWeMwsjSv9XhCOP1Tq3HZWASED8EnJ6ORW8t3PbVWWw386URzHoPGW5Fcisro-pB37NHLoK7xUvTA9rC42rh2b3Vx_obvHc6WnwT_qKDdpydRztPZo_EBjydSuRrrI3mWAfyOQETNaf4YLN8uIJC_Y1JDLjvz8697uJnBjdMed8NDVjw7y9ciXrcLq2haAr530r1qJe18KY9ud2pjNJ3XtPnMdLVkB36KAZ9_CNrGnPwI1tTSI0_OHeUgtqWhH8RNzM-hywF5skpKmJxKmXiDjUbuDVv3Hh5lqYrucrKY0diqMnbIEs3_Za-OM3od7psKOtCyAfrK1_IKp8k9yHJj-UXDr6UbWy4IwAkWtvfxOJ-eG_7Fqh4s6rqnlh6DsDIMztIlhb0PrwhNdQlenxRuXw9HNCP9GuNRhRCKYm1NCL0_5jdg0gB3qsPpbAFtYXeRzY7GcaE7YSOxMZaS-oNZL5fupikJY9UM9IuAIwEykSDddBkGkhIUG54WjGyDdg5e7d9q0jrAyNIqpTLVdyqtmWq-ms4f2RY4cCW2l8oaxauYcCXnGnYOn0ZgbLJiqYj4_pTFwo0s1-8HE8GkbpM41ZvnVcV3t5Jul2eLaa5XvdLMbXEz3AOxERL12QqtFvBP_DJbHVuwdfFgeLZ1iZqb3qLaWjWh4pMAshSsUgqfFyi7IY639B9Jgjf69HTHWeomOB6Q7RvgynoraYS93rtuPdE6o7uNXvfaFVJo2L9xyEcxN0WKVOdR50ulQ3dquC9GXe6nDYT_76I-pnsaYU4IfpvhwncvFGZOdVek7Sg8Al_fdBNigy07PhkJxJy9pDxXar_nTrRu9cborVvC5y4Ttywm2GKkIzCZg5kI0js-wPNXXgLoj5rNYZyxkfhaw6M5R4u_wJxdrReBW7fnWTyDwQsODMA-sOjwmBsIt4JOTgTH5wa_2FDEwVRZdqs2JvhPJjIKcYI9Ue6uTn2_RTbxeJviMrtVkn_92ETBZ9Or1Xy0T1RLYsc5Q--lf7xJ7U2XbVm6oIsVZ9QoN0TEHNVoePlF2EOAdudzxPdGAVYek3jd9Mcv9cT0H2javWNrfAc7g37VEh0l0ULm1t-pdLrGUXIkjy9Epv15EI8Hn-QUZ_l1Nio_IygwPCF_ntbytlDBEqERwR9rSeVsGWh3nTm_eumOS_paSaL5dt7xh1oe0oXWp_yamyFa7AXeRIqweEUsasIRpPWMAWh4"})
				res2 = sess.post('https://crud.api-world.co/api/v1/auth/login', json = {"email":email,"password":"Simpiser243#","worldId":"47580924-beb3-41ee-ac5c-8555fc7bdeb5","captchaToken":"03AAYGu2STVb5_8ayE12pX7evN80cg5uZLksSlHCMvI48hmRDJSR4rYD7ZV-OyZEv5EjitzTLChCppLjacWnjo9ikwle_WfVhlTg8OVPtwwMUz1WitSAE94C7G40nPGY6_D8ucKO4GWhhLUn6MFOHQZk8IpF6liJBEyJ6f3kGqwm74VMG7SZ0lvpDq1vZc3UeQOWFhZjnX7qaUrXVMDcFRVSJSAVn9nW_TbZ4HJfbzB1OPYL2f__lWyCw2YoA7oIS48gfiP43dNwvZBHwQ3FI17QNVKi4GfhxPf4ul73t8bPkcFDE95mOHFcODtl3_InoAt58a2yghUsPi_wU0f-dHCAlX2FQTBJ8GdsPjcUo8iuIjHFcmw3fgtS0IoNdyFcG6KKQ28_H97V7Rpdl51AqT9JRHSE_qKBK2oheQLzRRosFrPxx0tkZuwDjdt26RiRygRBmv3QDmX0yrxF-pekEjv0l_SOvtIYOBadFajCQmif2Gmz0xeKVzPeWe0yUI30r7uWWQFS_QHhyZIeIa-yipLs1KEJbKMhd79LX9wGpqlUuDv6uDVuIPvdHbWEKetQVlwsRRLHz5XLf7LUWt_Zqq7-DhS-pNzeV1cMpsyDOoslGrsPbKDKeJ1lGUNFAyoxgZIrWTl4tI9jEUO9SwdexUqyDU2ehmKmqZ2sWu96kXJeuGO_SEx_wVUDBSjaPC-BCJnMkyMk9rsHCQLDic3-Plgccf4CFb7HFZXEm06DVLe-221tlbHbzr7YGNFi6HUhsOPtZqjdnmS4h1BlIr9EwwQQiX5bA-lEpNPgRFLdTyjLBMla144S6KA0v8xq-MYu0-5mbiGUCqYNcg1K8dzxxRykYXaU2JwIhlG4LGfXY6DfrqaMhjyudk2TGhUeE6JPKhHzmDtPEKd7doDzLneGFY67witG3NnmE7iz_tBO_lr_mlNzuXlLWugq5GTVPyi71NMpWy6Pd7puJMGU8Nu05YioP0WVoHxGiktZRCOXbEwnWTkYu8SPkVmGGL0t62Ofw4TGaV-Yd_WfLXlX9eQIZ5q9m6oG3rUogkE9104KOynULOBViD3wsfWKBSFETzYb2hwmAlL5zBaCCURdRJTMySlfeFnJLNtEFS7AyQgnyeag3edL_aeb80kVnXN2XQ1GbS4qtq6pATDQTvyRJ65crsUuYhfZHMXPagkX7emD9SWWhHKeexksULLCUzr8gGqbuDrl7L68BblxAGfiMbOFAMtR3suI5V1Ao6iwxWczhN2ep5_hTw7Lfpv_6Xh1bCE4PAST1PsGI70V9Y4lWY-wWhcJ0waY0ysLrOMXEfDV3fFtPGjzMAmxP93attb_8sa5ZRxxPS-WxCY-GpkltUsPm4Jo5iiLIvrKAwFaXc4MaLtvRgi8nkq3khLPN4bCNktoR7Os_cMwGL_hqvwiuiGLLha9bMFZFkcyNG0LdhJPqecgb6TVIIunYfrF7LJ8z4tS_BHYTRbyFuvFyLkM5khsccTP8Aa-5sWRGFZBEenkOA7p89h7o80kCtddPRN3TIYICzM4Vj5CIzN56EaRCuh-SNTQ4MCtZe_RLxzng0yDzUVpu-VKWZa401V__2VGkaTK-sm5ylsSdSCj7qaaaISYCjO_PUed5hWAYVyaKm9TKW-iIzA8kDiH_RArY"})
				token = res1.json()['token']
				headers = {'Authorization': f'Bearer {token}'}
				out = sess.post(f'https://crud.api-world.co/api/v1/worlds/threads/interact/{args.id}', json = {"type":"upvote"}, headers=headers)
				counter = out.json()['outputThreadMessage']['upvotesCount']
				print(f'\nTotal likes: {counter}')
		except KeyboardInterrupt:
			print("Exiting...")
			break
		except:
			print("Rate limited wait a minute...")
			time.sleep(args.cooldown)

if __name__ == "__main__":
	parser = argparse.ArgumentParser(description='Adding more likes to your post')
	parser.add_argument('--id', type=str, help='Post id')
	parser.add_argument('--max_likes', type=int, default=1000, help='Max amount of likes that post will get')
	parser.add_argument('--cooldown', type=int, default=60, help='Cooldown in seconds')
	args = parser.parse_args()
	more_likes(args)
