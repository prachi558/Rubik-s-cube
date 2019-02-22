import numpy as np
import cv2
import A

cap_1 = cv2.VideoCapture(1)
#cap_2 = cv2.VideoCapture(2)
i = 0


while True:

	ret,img = cap_1.read()
	image_2 = img


	if i == 30:

		F_L_W =[40,3,180]
		F_U_W =[110,18,240]

		F_L_R =[2,200,140]
		F_U_R =[5,245,200]

		F_L_Y =[15,185,200]
		F_U_Y =[25,225,260]

		F_L_BLK =[45,75,0]
		F_U_BLK =[90,160,60]

		U_L_W =[40,0,210]
		U_U_W =[110,50,255]

		U_L_R =[2,0,0]
		U_U_R =[16,0,0]

		U_L_Y =[15,0,0]
		U_U_Y =[29,0,0]

		U_L_BLK =[0,0,90]
		U_U_BLK =[95,35,170]

		# R_L_W =[35,0,150]
		# R_U_W =[60,20,225]

		# R_L_R =[2,0,0]
		# R_U_R =[16,0,0]

		# R_L_Y =[15,0,0]
		# R_U_Y =[26,0,0]

		# R_L_BLK =[55,15,0]
		# R_U_BLK =[100,100,60]

		B_L_W =[48,5,150]
		B_U_W =[66,20,180]

		B_L_R =[4,0,0]
		B_U_R =[7,0,0]

		B_L_Y =[15,0,0]
		B_U_Y =[26,0,0]

		B_L_BLK =[30,15,30]
		B_U_BLK =[60,65,100]

		# L_L_W =[70,0,160]
		# L_U_W =[95,20,250]

		# L_L_R =[5,0,0]
		# L_U_R =[16,0,0]

		# L_L_Y =[15,0,0]
		# L_U_Y =[26,0,0]

		# L_L_BLK =[20,0,0]
		# L_U_BLK =[100,30,160]

		# D_L_W =[80,8,0]
		# D_U_W =[95,24,0]

		# D_L_R =[2,0,0]
		# D_U_R =[14,0,0]

		# D_L_Y =[19,0,0]
		# D_U_Y =[26,0,0]

		# D_L_BLK =[0,0,0]
		# D_U_BLK =[80,80,0]

		


		cv2.imwrite('BGR_IMG.jpg',img)
		img_hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
		cv2.imwrite('HSV_IMG.jpg',img_hsv)

		roi_2 = cv2.imread('BGR_IMG.jpg')
		roi_1 = cv2.imread('HSV_IMG.jpg')

		F1 = roi_1[240:274, 152:171]
		F2 = roi_1[255:277, 200:227]
		F3 = roi_1[277:296, 270:305]
		F4 = roi_1[311:336, 146:166]
		F6 = roi_1[349:367, 270:301]
		F7 = roi_1[404:419, 181:192]
		F8 = roi_1[398:435, 218:248]
		F9 = roi_1[426:463, 280:314]


		U1 = roi_1[157:164, 262:264]
		U2 = roi_1[172:178, 325:342]
		U3 = roi_1[185:198, 384:405]
		U4 = roi_1[179:186, 221:249]
		U6 = roi_1[203:213, 351:375]
		U7 = roi_1[202:212, 172:204]
		U8 = roi_1[215:230, 230:270]
		U9 = roi_1[225:235, 309:333]


		R1 = roi_1[275:311, 335:352]
		R2 = roi_1[252:275, 378:400]
		R3 = roi_1[229:252, 418:434]
		R4 = roi_1[350:379, 338:353]
		R6 = roi_1[292:305, 416:427]
		R7 = roi_1[431:448, 335:349]
		R8 = roi_1[390:410, 380:392]
		R9 = roi_1[374:386, 409:418]

		D1 = roi_1[425:436, 366:393]

		D2 = roi_1[445:450, 313:329]

		D3 = roi_1[451:454, 235:240]

		D4 = roi_1[383:392, 319:333]

		D6 = roi_1[425:435, 190:198]

		D7 = roi_1[354:370, 255:276]

		D8 = roi_1[381:392, 179:202]

		D9 = roi_1[397:401, 122:133]

		#HSV average

		d1 = A.avg(D1)
		d2 = A.avg(D2)
		d3 = A.avg(D3)
		d4 = A.avg(D4)
		d6 = A.avg(D6)
		d7 = A.avg(D7)
		d8 = A.avg(D8)
		d9 = A.avg(D9)
		D=[d1,d2,d3,d4,d6,d7,d8,d9]

		D_1 = roi_2[425:436, 366:393]

		D_2 = roi_2[445:450, 313:329]

		D_3 = roi_2[451:454, 235:240]

		D_4 = roi_2[383:392, 319:333]

		D_6 = roi_2[425:435, 190:198]

		D_7 = roi_2[354:370, 255:276]

		D_8 = roi_2[381:392, 179:202]

		D_9 = roi_2[397:401, 122:133]

		#BGR average

		d_1 = A.avg(D_1)
		d_2 = A.avg(D_2)
		d_3 = A.avg(D_3)
		d_4 = A.avg(D_4)
		d_6 = A.avg(D_6)
		d_7 = A.avg(D_7)
		d_8 = A.avg(D_8)
		d_9 = A.avg(D_9)
		D_bgr=[d_1,d_2,d_3,d_4,d_6,d_7,d_8,d_9]

		L1 = roi_1[128:138, 319:337]

		L2 = roi_1[168:188, 372:390]

		L3 = roi_1[201:210, 411:420]

		L4 = roi_1[193:222, 314:329]

		L6 = roi_1[277:301, 422:435]

		L7 = roi_1[274:301, 313:338]

		L8 = roi_1[310:336, 368:390]

		L9 = roi_1[354:379, 420:438]

		l1 = A.avg(L1)
		l2 = A.avg(L2)
		l3 = A.avg(L3)
		l4 = A.avg(L4)
		l6 = A.avg(L6)
		l7 = A.avg(L7)
		l8 = A.avg(L8)
		l9 = A.avg(L9)
		L=[l1,l2,l3,l4,l6,l7,l8,l9]

		L_1 = roi_2[128:138, 319:337]

		L_2 = roi_2[168:188, 372:390]

		L_3 = roi_2[201:210, 411:420]

		L_4 = roi_2[193:222, 314:329]

		L_6 = roi_2[277:301, 422:435]

		L_7 = roi_2[274:301, 313:338]

		L_8 = roi_2[310:336, 368:390]

		L_9 = roi_2[354:379, 420:438]

		l_1 = A.avg(L_1)
		l_2 = A.avg(L_2)
		l_3 = A.avg(L_3)
		l_4 = A.avg(L_4)
		l_6 = A.avg(L_6)
		l_7 = A.avg(L_7)
		l_8 = A.avg(L_8)
		l_9 = A.avg(L_9)
		L_bgr=[l_1,l_2,l_3,l_4,l_6,l_7,l_8,l_9]

		B1 = roi_1[177:183, 153:162]

		B2 = roi_1[166:187, 183:211]

		B3 = roi_1[136:149, 244:275]

		B4 = roi_1[257:275, 116:136]

		B6 = roi_1[197:215, 240:267]

		B7 = roi_1[331:353, 105:123]

		B8 = roi_1[310:332, 163:192]

		B9 = roi_1[281:301, 233:264]

		b1 = A.avg(B1)
		b2 = A.avg(B2)
		b3 = A.avg(B3)
		b4 = A.avg(B4)
		b6 = A.avg(B6)
		b7 = A.avg(B7)
		b8 = A.avg(B8)
		b9 = A.avg(B9)
		B=[b1,b2,b3,b4,b6,b7,b8,b9]

		B_1 = roi_2[177:183, 153:162]

		B_2 = roi_2[166:187, 183:211]

		B_3 = roi_2[136:149, 244:275]

		B_4 = roi_2[257:275, 116:136]

		B_6 = roi_2[197:215, 240:267]

		B_7 = roi_2[331:353, 105:123]

		B_8 = roi_2[310:332, 163:192]

		B_9 = roi_2[281:301, 233:264]

		b_1 = A.avg(B_1)
		b_2 = A.avg(B_2)
		b_3 = A.avg(B_3)
		b_4 = A.avg(B_4)
		b_6 = A.avg(B_6)
		b_7 = A.avg(B_7)
		b_8 = A.avg(B_8)
		b_9 = A.avg(B_9)
		B_bgr=[b_1,b_2,b_3,b_4,b_6,b_7,b_8,b_9]





		# F_1 = roi_2[240:274, 152:171]
		# F_2 = roi_2[255:277, 200:227]
		# F_3 = roi_2[277:296, 270:305]
		# F_4 = roi_2[311:336, 146:166]
		# F_6 = roi_2[349:367, 270:301]
		# F_7 = roi_2[404:419, 181:192]
		# F_8 = roi_2[398:435, 218:248]
		# F_9 = roi_2[426:463, 280:314]


		# U_1 = roi_2[157:164, 262:264]
		# U_2 = roi_2[172:178, 325:342]
		# U_3 = roi_2[185:198, 384:405]
		# U_4 = roi_2[179:186, 221:249]
		# U_6 = roi_2[203:213, 351:375]
		# U_7 = roi_2[202:212, 172:204]
		# U_8 = roi_2[215:230, 230:270]
		# U_9 = roi_2[225:235, 309:333]


		# R_1 = roi_2[275:311, 335:352]
		# R_2 = roi_2[252:275, 378:400]
		# R_3 = roi_2[229:252, 418:434]
		# R_4 = roi_2[350:379, 338:353]
		# R_6 = roi_2[292:305, 416:427]
		# R_7 = roi_2[431:448, 335:349]
		# R_8 = roi_2[390:410, 380:392]
		# R_9 = roi_2[374:386, 409:418]

		# r1 = A.avg(R1)
		# r2 = A.avg(R2)
		# r3 = A.avg(R3)
		# r4 = A.avg(R4)
		# r6 = A.avg(R6)
		# r7 = A.avg(R7)
		# r8 = A.avg(R8)
		# r9 = A.avg(R9)


		# u1 = A.avg(U1)
		# u2 = A.avg(U2)
		# u3 = A.avg(U3)
		# u8 = A.avg(U8)
		# u9 = A.avg(U9)
		# u4 = A.avg(U4)
		# u6 = A.avg(U6)
		# u7 = A.avg(U7)

		# f1 = A.avg(F1)
		# f2 = A.avg(F2)
		# f3 = A.avg(F3)
		# f4 = A.avg(F4)
		# f6 = A.avg(F6)
		# f7 = A.avg(F7)
		# f8 = A.avg(F8)
		# f9 = A.avg(F9)

		# F=[f1,f2,f3,f4,f6,f7,f8,f9]
		# U=[u1,u2,u3,u4,u6,u7,u8,u9]
		# R=[r1,r2,r3,r4,r6,r7,r8,r9]

		# f_1 = A.avg(F_1)
		# f_2 = A.avg(F_2)
		# f_3 = A.avg(F_3)
		# f_4 = A.avg(F_4)
		# f_6 = A.avg(F_6)
		# f_7 = A.avg(F_7)
		# f_8 = A.avg(F_8)
		# f_9 = A.avg(F_9)

		# r_1 = A.avg(R_1)
		# r_2 = A.avg(R_2)
		# r_3 = A.avg(R_3)
		# r_4 = A.avg(R_4)
		# r_6 = A.avg(R_6)
		# r_7 = A.avg(R_7)
		# r_8 = A.avg(R_8)
		# r_9 = A.avg(R_9)


		# u_1 = A.avg(U_1)
		# u_2 = A.avg(U_2)
		# u_3 = A.avg(U_3)
		# u_8 = A.avg(U_8)
		# u_9 = A.avg(U_9)
		# u_4 = A.avg(U_4)
		# u_6 = A.avg(U_6)
		# u_7 = A.avg(U_7)


		# F_bgr = [f_1,f_2,f_3,f_4,f_6,f_7,f_8,f_9]
		# U_bgr = [u_1,u_2,u_3,u_4,u_6,u_7,u_8,u_9]
		# R_bgr = [r_1,r_2,r_3,r_4,r_6,r_7,r_8,r_9]


		a = 1
		b = 1
		c = 1
		z = 1
		q = 1
		r = 1
		arr = []
		arr2 = []
		arr3 =[]


		for j in F_bgr:
			blue = j[0]
			green = j[1]
			red = j[2]
			if (blue/red>2) and (blue/green>2):
				arr.append(a)
				print(a)
				print(j)
				print(' is blue')
			elif (green/red>2) & (green>100):
				arr.append(a)
				print(a)
				print(j)
				print(' is green')
			elif (red/blue>2) & (red/green>2) & (red>100) :
				arr.append(a)  #& (red>100)
				print(a)
				print(j)
				print(' is red')
			else:
				arr.append(0)
			a+=1

		#print(arr)



		# arr4 =[]
		# for j in U_bgr:
		# 	blue2 = j[0]
		# 	green2 = j[1]
		# 	red2 = j[2]
		# 	#print(j)
		# 	if (blue2/red2>1.2) & (blue2/green2>1.2) &  (blue2>80):
		# 		arr4.append(b)
		# 		print(b)
		# 		print(j)
		# 		print(' is blue')
		# 	elif (green2/red2>1) & (green2/blue2>1.2) :
		# 		arr4.append(b)
		# 		print(b)
		# 		print(j)
		# 		print(' is green')
		# 	elif (red2/blue2>1.3) & (red2/green2>1.3) : 
		# 		arr4.append(b) #& (red>100)
		# 		print(b)
		# 		print(j)
		# 		print(' is red')
		# 	else:
		# 		arr4.append(0)
		# 	b+=1

			
		# for j in R_bgr:
		# 	blue3 = j[0]
		# 	green3 = j[1]
		# 	red3 = j[2]
		# 	if (blue3/red3>1) and (blue3/green3>1) & (205>blue3>100):
		# 		arr2.append(c)
		# 		print(c)
		# 		print(j)
		# 		print(' is blue')
		# 	elif (green3/red3>2) & (green3>100):
		# 		arr2.append(c)
		# 		print(c)
		# 		print(j)
		# 		print(' is green')
		# 	elif (red3/blue3>2) & (red3/green3>2) : 
		# 		arr2.append(c) #& (red>100)
		# 		print(c)
		# 		print(j)
		# 		print(' is red')
		# 	else:
		# 		arr2.append(0)
		# 	c+=1

		# print(arr2)	

		# arr4 =[]
		# q = 1
		# for j in B_bgr:
		# 	blue = j[0]
		# 	green = j[1]
		# 	red = j[2]
		# 	if (blue/red>1) and (blue/green>1) & (blue<210):
		# 		arr4.append(q)
		# 		print(q)
		# 		print(j)
		# 		print(' is blue')
		# 	elif (green/red>1) & (green/blue>1.3) & (200>green>100):
		# 		arr4.append(q)
		# 		print(q)
		# 		print(j)
		# 		print(' is green')
		# 	elif (red/blue>1.3) & (red/green>1.4) & (red>50) :
		# 		arr4.append(q)  #& (red>100)
		# 		print(q)
		# 		print(j)
		# 		print(' is red')
		# 	else:
		# 		arr4.append(0)
		# 	q+=1

		# print(arr4)
		# for j in L_bgr:
		# 	blue5 = j[0]
		# 	green5 = j[1]
		# 	red5 = j[2]
		# 	#print((j))
		# 	if (blue5/red5>1.5) and (blue5/green5>1.5) & (blue5<200):
		# 		arr3.append(q)
		# 		print(q)
		# 		print(j)
		# 		print(' is blue')
		# 	elif (green5/red5>1.5) & (green5>50):
		# 		arr3.append(q)
		# 		print(q)
		# 		print(j)
		# 		print(' is green')
		# 	elif (red5/blue5>1.5) & (red5/green5>1.5) & (red5>100) :
		# 		arr3.append(q)  #& (red>100)
		# 		print(q)
		# 		print(j)
		# 		print(' is red')
		# 	else:
		# 		arr3.append(0)
		# 	q+=1

		# print(arr3)
		# for j in D_bgr:
		# 	blue6 = j[0]
		# 	green6 = j[1]
		# 	red6 = j[2]
		# 	if (blue6/red6>1) and (blue6/green6>1):
		# 		print(r)
		# 		print(j)
		# 		print(' is blue')
		# 	elif (green6/red6>1) & (green6>90):
		# 		print(r)
		# 		print(j)
		# 		print(' is green')
		# 	elif (red6/blue6>1.2) & (red6/green6>1.2) & (red6>50) :  #& (red>100)
		# 		print(r)
		# 		print(j)
		# 		print(' is red')
		# 	r+=1




		p = 1
		for j in F:
			if p == arr[p-1]:
				pass 
			else:

				if  (int(j[0]) in range(F_L_Y[0],F_U_Y[0])):
					print(p)
					print (j)
					print(' is yellow')
				elif  (int(j[1]) in range(F_L_W[1],F_U_W[1])) & (int(j[2]) in range(F_L_W[2],F_U_W[2])):
					print(p)
					print(j)
					print(' is white')
				else :
					print(p)
					print(j)
					print(' is black')

		 	p+=1

		v = 1
		for j in R:
			if v == arr2[v-1]:
				pass 
			else:

				if  (int(j[0]) in range(R_L_Y[0],R_U_Y[0])):
					print(v)
					print (j)
					print(' is yellow')
				elif (int(j[1]) in range(R_L_W[1],R_U_W[1])) & (int(j[2]) in range(R_L_W[2],R_U_W[2])):
					print(v)
					print(j)
					print(' is white')
				else :
					print(v)
					print(j)
					print(' is black')

			v+=1

		# h = 1
		# for j in L:
		# 	# if (int(j[0]) in range(F_L_R[0],F_U_R[0])):
		# 	# 	print(p)
		# 	# 	print(j)
		# 	# 	print(' is red')
		# 	if h == arr3[h-1]:
		# 		pass 
		# 	else:

		# 		if  (int(j[0]) in range(L_L_Y[0],L_U_Y[0])):
		# 			print(h)
		# 			print (j)
		# 			print(' is yellow')
		# 		elif  (int(j[1]) in range(L_L_BLK[1],L_U_BLK[1])) & (int(j[2]) in range(L_L_BLK[2],L_U_BLK[2])):
		# 			print(h)
		# 			print(j)
		# 			print(' is black')
		# 		else :
		# 			print(h)
		# 			print(j)
		# 			print(' is white')

		# 	h+=1


		x = 1
		for j in U:
			if x == arr4[x-1]:
				pass 
			else:

				if  (int(j[0]) in range(U_L_Y[0],U_U_Y[0])):
					print(x)
					print (j)
					print(' is yellow')
				elif  (int(j[1]) in range(U_L_BLK[1],U_U_BLK[1])) & (int(j[2]) in range(U_L_BLK[2],U_U_BLK[2])):
					print(x)
					print(j)
					print(' is black')
				else :
					print(x)
					print(j)
					print(' is white')

			x+=1

		# y = 1
		# for j in B:
		# 	# if (int(j[0]) in range(F_L_R[0],F_U_R[0])):
		# 	# 	print(p)
		# 	# 	print(j)
		# 	# 	print(' is red')
		# 	if y == arr4[y-1]:
		# 		pass 
		# 	else:

		# 		if  (int(j[0]) in range(B_L_Y[0],B_U_Y[0])):
		# 			print(y)
		# 			print (j)
		# 			print(' is yellow')
		# 		elif  (int(j[1]) in range(B_L_BLK[1],B_U_BLK[1])) & (int(j[2]) in range(B_L_BLK[2],B_U_BLK[2])):
		# 			print(y)
		# 			print(j)
		# 			print(' is black')
		# 		else :
		# 			print(y)
		# 			print(j)
		# 			print(' is white')

		# 	y+=1




	i+=1

	#up

	# image_2[157:164, 262:264] = [255, 255, 255]
	# image_2[172:178, 325:342] = [255, 255, 255]
	# image_2[185:198, 384:405] = [255, 255, 255]
	# image_2[179:186, 221:249] = [255, 255, 255]
	# image_2[203:213, 351:375] = [255, 255, 255]
	# image_2[202:212, 172:204] = [255, 255, 255]
	# image_2[215:230, 230:270] = [255, 255, 255]
	# image_2[225:235, 309:333] = [255, 255, 255]


	# # # #front

	# image_2[240:274, 152:171] = [255, 255, 255]
	# image_2[255:277, 200:227] = [255, 255, 255]
	# image_2[277:296, 270:305] = [255, 255, 255]
	# image_2[311:336, 146:166] = [255, 255, 255]
	# image_2[349:367, 270:301] = [255, 255, 255]
	# image_2[404:419, 181:192] = [255, 255, 255]
	# image_2[398:435, 218:248] = [255, 255, 255]
	# image_2[426:463, 280:314] = [255, 255, 255]

	# # # #right

	# image_2[275:311, 335:352] = [255, 255, 255]
	# image_2[252:275, 378:400] = [255, 255, 255]
	# image_2[229:252, 418:434] = [255, 255, 255]
	# image_2[350:379, 338:353] = [255, 255, 255]
	# image_2[292:305, 416:427] = [255, 255, 255]
	# image_2[431:448, 335:349] = [255, 255, 255]
	# image_2[390:410, 380:392] = [255, 255, 255]
	# image_2[374:386, 409:418] = [255, 255, 255]

		#down

	image_2[425:436, 366:393] = [255, 255, 255]
	image_2[445:450, 313:329] = [255, 255, 255]
	image_2[451:454, 235:240] = [255, 255, 255]
	image_2[383:392, 319:333] = [255, 255, 255]
	image_2[425:435, 190:198] = [255, 255, 255]
	image_2[354:370, 255:276] = [255, 255, 255]
	image_2[381:392, 179:202] = [255, 255, 255]
	image_2[397:401, 122:133] = [255, 255, 255]
	
	# # #left	

	image_2[128:138, 319:337] = [255, 255, 255]
	image_2[168:188, 372:390] = [255, 255, 255]
	image_2[201:210, 414:420] = [255, 255, 255]
	image_2[193:222, 314:329] = [255, 255, 255]
	image_2[277:301, 422:435] = [255, 255, 255]
	image_2[274:301, 313:338] = [255, 255, 255]
	image_2[310:336, 368:390] = [255, 255, 255]
	image_2[354:379, 420:438] = [255, 255, 255]


	# # #back

	image_2[177:183, 153:162] = [255, 255, 255]
	image_2[166:187, 183:211] = [255, 255, 255]
	image_2[136:149, 244:275] = [255, 255, 255]
	image_2[257:275, 116:136] = [255, 255, 255]
	image_2[197:215, 240:267] = [255, 255, 255]
	image_2[331:353, 105:123] = [255, 255, 255]
	image_2[310:332, 163:192] = [255, 255, 255]
	image_2[281:301, 233:264] = [255, 255, 255]

	cv2.imshow('img',image_2)

	if cv2.waitKey(1) & 0xFF== ord('q'):
		break



cap_1.release()
cv2.destroyAllWindows()
