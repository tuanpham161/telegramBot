def dothi(message):
	a = []
	b = []
	bieuthuc = ""
	a = message.split('(')
	b = a[1].split(' ')
	b[len(b) - 1] = b[len(b) - 1].replace(")", "")
	for i in range(len(b)):
		b[i] = int(b[i])
	for i in range(len(b)):
		if i != len(b) - 1:
			bieuthuc = bieuthuc + str(b[i]) + ".x^" + str(len(b) - i - 1) + " + "
		if i == len(b) - 1:
			bieuthuc = bieuthuc + str(b[len(b) - 1])
	bot.send_message(990978363,"Đồ thị hàm số " +"\n"+"y = "+bieuthuc)
	y=0
	x=np.linspace(-4,4,100)
	for i in range(len(b)):
		y= y+ b[i]*x**(len(b)-i-1)
	plt.plot(x,y)
	plt.show()


@bot.message_handler(commands=['math'] )
def chart_math(message):
	dothi(message.text)