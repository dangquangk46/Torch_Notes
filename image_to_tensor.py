#std is standard deviation
#mean is mean value
img = Image.open('PATH')
x = transform(img)

z = x * torch.tensor(std).view(3, 1, 1)
z = z + torch.tensor(mean).view(3, 1, 1)

img2 = transforms.ToPILImage(mode='RGB')(z)
plt.imshow(img2)
