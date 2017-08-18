import torchvision.models as models

print('Checking models...')
print(models.resnet18())
print(models.alexnet())
print(models.vgg16())
print(models.squeezenet1_0())

print('Checking pretrained models...')
# print(models.resnet18(pretrained=True))
# print(models.alexnet(pretrained=True))
print(models.squeezenet1_0(pretrained=True))
