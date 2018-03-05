from django.contrib.auth.models import User, Group
from django.db.models import Q
from rest_framework.exceptions import ValidationError
from rest_framework.serializers import ModelSerializer, HyperlinkedIdentityField, SerializerMethodField, CharField
from shop.models import Product , AllMobilePhoneSpecification, Buyer, Order
from rest_framework import serializers


class UserDetailSerializer(ModelSerializer):
    class Meta:
        model = Buyer
        fields = ['seller','name','email','city','phone_number','address','zip_code','state','country','DOB','photo',]



class UserCreateSerializer(ModelSerializer):
    buyer = UserDetailSerializer()



    class Meta:
        model = User
        fields = ['username','password','email','buyer']
        extra_kwargs = {"password":{"write_only":True}

        }

    def validate(self, data):

        username = data['username']
        user_qs = User.objects.filter(username = username)
        if user_qs.exists():
            raise ValidationError("This user already exist")
        return data



    def create(self, validated_data):
        username = validated_data['username']
        email = validated_data['email']
        password = validated_data['password']
        buyer_data = validated_data.pop('buyer')
        user_obj = User(username=username, email=email)

        user_obj.set_password(password)
        user_obj.save()

        Buyer.objects.create(user=user_obj, **buyer_data)
        return user_obj





class UserLoginSerializer(ModelSerializer):
    username = CharField(label='Username')
    token = CharField(allow_blank=True, read_only=True)
    class Meta:
        model = User
        fields = ['username',
                  'password',
                  'token']
        extra_kwargs = {"password":{"write_only":True}

        }

    def validate(self, data):
        user_obj = None
        username = data.get("username",None)
        password = data["password"]
        if not username:
            raise ValidationError("Username required")

        user = User.objects.filter(
            Q(username = username)
        ).distinct()

        if user.exists() and user.count() == 1:
            user_obj = user.first()
        else:
            raise ValidationError("Useranme not valid")

        if user_obj:
            if not user_obj.check_password(password):
                raise ValidationError("Incorrect credentials")

        data["token"] = "some random token"


        return data








class AllMobilePhoneSpecificationSerializer(ModelSerializer):
    class Meta:
        model = AllMobilePhoneSpecification
        fields = '__all__'




class ProductListSerializer(ModelSerializer):
    # url = HyperlinkedIdentityField(
    #     view_name='shop-api:productDetail',
    #     lookup_field='product_id'
    # )
    # delete_url = HyperlinkedIdentityField(
    #     view_name='shop-api:productDelete',
    #     lookup_field='product_id'
    # )
    seller = SerializerMethodField()
    # image = SerializerMethodField()
    specification = SerializerMethodField()

    class Meta:
        model = Product
        fields = '__all__'

    def get_seller(self,obj):
        return str(obj.seller.name)
    # def get_image(self,obj):
    #     return obj.image.url
    def get_specification(self,obj):
        try:
            specification_qs = AllMobilePhoneSpecification.objects.filter(product=obj)
        except:
            specification_qs = None
        specification = AllMobilePhoneSpecificationSerializer(specification_qs,many=True).data
        return specification




class ProductDetailSerializer(ModelSerializer):
    seller = SerializerMethodField()
    image = SerializerMethodField()
    specification = SerializerMethodField()
    class Meta:
        model = Product
        fields = '__all__'

    def get_seller(self, obj):
        return str(obj.seller.name)

    def get_image(self, obj):
        return obj.image.url

    def get_specification(self, obj):
        try:
            specification_qs = AllMobilePhoneSpecification.objects.filter(product=obj)
        except:
            specification_qs = None
        specification = AllMobilePhoneSpecificationSerializer(specification_qs, many=True).data
        return specification


class ProductCreateSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ['product_subcatagory','product_id','brand','name','mrp','price','short_desc','full_desc','image']

class OrderCreateSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = ['Order_id','seller','buyer','product','total_cost','shipping_address','city','pin_code','payment_status','order_status','payment_mode']




