from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
import datetime


# Create your models here.



class SellerCatagory(models.Model):
    SELLER_CATAGORY_LIST = (
        ('AUTOMOTIVE', 'Automotive'),
        ('BABY PRODUCTS', 'Baby Products'),
        ('BEAUTY', 'Beauty'),
        ('BOOKS ', 'Books'),
        ('CAMERA AND ACCESSORIES ', 'Camera and Accessories'),
        ('CLOTHING AND ACCESSORIES', 'Clothing and Accessories'),
        ('COMPUTER AND ACCESSORIES', 'Computer and Accessories'),
        ('CONSUMER ELECTRONICS', 'Consumer Electronics'),
        ('EVERYTHING ELSE ', 'Everything Else'),
        ('FINE ART', 'Fine Art'),
        ('FURNITURE', 'Furniture'),
        ('GIFT CARD', 'Gift Card'),
        ('GROCERY AND GOURMET FOOD', 'Grocery and Gourmet Food'),
        ('HANDBAGS', 'Handbags'),
        ('HEALTH AND PERSONAL CARE', 'Health and Personal Care'),
        ('HOME AND GARDEN', 'Home and Garden'),
        ('INDUSTRIAL AND SCIENTIFIC SUPPLY', 'Industrial and Scientific Supply'),
        ('JEWELRY', 'Jewelry'),
        ('KITCHEN', 'Kitchen'),
        ('LUGGAGE AND TRAVEL ACCESSORIES ', 'Luggage and Travel Accessories'),
        ('MOBILE AND ACCESSORIES', 'Mobile and Accessories'),
        ('MOVIES AND DVD', 'Movies and DVD'),
        ('MUSIC', 'Music'),
        ('MUSICAL INSTRUMENTS ', 'Musical Instruments'),
        ('OFFICE PRODUCTS', 'Office Products'),
        ('PET PRODUCTS', 'Pet Products'),
        ('SHOES', 'Shoes'),
        ('SOFTWARE', 'Software'),
        ('SPORTS AND OUTDOORS', 'Sports and Outdoors'),
        ('SUNGLASSES AND EYEWEAR', 'Sunglasses and Eyewear'),
        ('TOOLS AND HOME IMPROVEMENT', 'Tools and Home Improvement'),
        ('TOYS AND GAMES', 'Toys and Games'),
        ('VIDEO GAMES', 'Video Games'),
        ('WATCHES', 'Watches'),

    )
    catagory = models.CharField(choices=SELLER_CATAGORY_LIST, max_length=254, blank= True,   unique=True)
    other_catagory = models.CharField(max_length=254, blank=True ,  )

    def __str__(self):
        if (self.catagory):
            return str(self.catagory)
        else:
            return str(self.other_catagory)

class Seller(models.Model):
    GENDER =(
        ('M','male'),
        ('F', 'female'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(default=None)
    catagory = models.ForeignKey(SellerCatagory, default=None)
    name = models.CharField(max_length=254, default=None)
    gender = models.CharField(choices=GENDER, max_length=10, default=None)
    DOB = models.DateField(default=None)
    address = models.CharField(max_length=500, default=None)
    city = models.CharField(max_length=50, default=None)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=10, default=None )
    image = models.ImageField(default=None)
    registeration_date = models.DateField(default=datetime.date.today())
    active = models.BooleanField(default=1)

    def __str__(self):
        return str(self.user)


class Buyer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    seller = models.ForeignKey(Seller)
    name = models.CharField(max_length=254, default=None)
    email = models.EmailField(default=None)
    city = models.CharField(default=None , max_length=254)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")


    phone_number = models.CharField(validators=[phone_regex], max_length=10, default=None)
    address = models.TextField(default=None, max_length=1000)
    zip_code = models.IntegerField(default=None)
    state = models.CharField(default=None, max_length=254)
    country = models.CharField(default=None, max_length=254)
    DOB = models.DateField(default=datetime.date.today())
    photo = models.ImageField()

    def __str__(self):
        return str(self.name)








class ProductCatagory(models.Model):
    PRODUCT_CATAGORY_LIST = (

        ('MOBILES, COMPUTERS','Mobiles, Computers'),
        ('TV, APPLIANCES, ELECTRONICS','TV, Appliances, Electronics'),
        ('MEN\'S FASHION','Men\'s Fashion'),
        ('WOMEN\'S FASHION','Women\'s Fashion'),
        ('HOME, KITCHEN, PETS','Home, Kitchen, Pets'),
        ('BEAUTY, HEALTH, GROCERY','Beauty, Health, Grocery'),
        ('SPORTS, FITNESS, BAGS, LUGGAGE','Sports, Fitness, Bags, Luggage'),
        ('TOYS, BABY PRODUCTS, KIDS\' FASHION','Toys, Baby Products, Kids\' Fashion'),
        ('CAR, MOTORBIKE, INDUSTRIAL','Car, Motorbike, Industrial'),
        ('BOOKS','Books'),
        ('MOVIES, MUSIC & VIDEO GAMES','Movies, Music & Video Games'),
        ('GIFT CARDS','Gift Cards'),
        ('GLOBAL STORE','Global Store'),


    )
    catagory = models.CharField(choices=PRODUCT_CATAGORY_LIST, max_length=254, blank= True,unique=True, )
    other_catagory = models.CharField(max_length=254, blank=True, )

    def __str__(self):
        if (self.catagory):
            return str(self.catagory)
        else:
            return str(self.other_catagory)


class ProductSubcatagory(models.Model):
    PRODUCT_SUBCATAGORY_LIST = (


        ('ALL MOBILE PHONES','All Mobile Phones'),
        ('ALL MOBILE ACCESSORIES','All Mobile Accessories'),
        ('CASES & COVERS','Cases & Covers'),
        ('SCREEN PROTECTORS','Screen Protectors'),
        ('POWER BANKS','Power Banks'),
        ('USED & REFURBISHED MOBILES','Used & Refurbished Mobiles'),
        ('TABLETS','Tablets'),
        ('WEARABLE DEVICES','Wearable Devices'),
        (' SOFTWARE ',' Software '),
        ('OFFICE SUPPLIES & STATIONERY','Office Supplies & Stationery'),
        (' ALL COMPUTERS & ACCESSORIES ',' All Computers & Accessories '),
        ('LAPTOPS','Laptops'),
        ('DESKTOPS & MONITORS','Desktops & Monitors'),
        (' COMPUTER ACCESSORIES ',' Computer Accessories '),
        ('PEN DRIVES & MEMORY CARDS','Pen Drives & Memory Cards'),
        ('PRINTERS & INK','Printers & Ink'),


        (' ALL ELECTRONICS ',' All Electronics '),



        ('TELEVISIONS','Televisions'),
        ('HOME ENTERTAINMENT SYSTEMS','Home Entertainment Systems'),
        ('HEADPHONES','Headphones'),
        ('SPEAKERS','Speakers'),
        ('MP3, MEDIA PLAYERS & ACCESSORIES','MP3, Media Players & Accessories'),
        ('AUDIO & VIDEO ACCESSORIES','Audio & Video Accessories'),
        ('CAMERAS','Cameras'),
        ('DSLR CAMERAS','DSLR Cameras'),
        ('CAMERA ACCESSORIES','Camera Accessories'),
        ('MUSICAL INSTRUMENTS & PROFESSIONAL AUDIO','Musical Instruments & Professional Audio'),
        ('GAMING CONSOLES','Gaming Consoles'),
        (' ALL ELECTRONICS ',' All Electronics '),
        ('AIR CONDITIONERS','Air Conditioners'),
        ('REFRIGERATORS','Refrigerators'),
        ('WASHING MACHINES','Washing Machines'),
        ('KITCHEN & HOME APPLIANCES','Kitchen & Home Appliances'),
        ('HEATING & COOLING APPLIANCES','Heating & Cooling Appliances'),
        ('ALL APPLIANCES','All Appliances'),



        ('CLOTHING','Clothing'),
        ('T-SHIRTS & POLOS','T-shirts & Polos'),
        ('SHIRTS','Shirts'),
        ('JEANS','Jeans'),
        ('INNERWEAR','Innerwear'),
        ('WATCHES','Watches'),
        ('BAGS & BACKPACKS','Bags & Backpacks'),
        ('SUNGLASSES','Sunglasses'),
        ('JEWELLERY','Jewellery'),
        ('WALLETS','Wallets'),
        ('SHOES','Shoes'),
        ('SPORTS SHOES','Sports Shoes'),
        ('FORMAL SHOES','Formal Shoes'),
        ('CASUAL SHOES','Casual Shoes'),
        ('SPORTSWEAR','Sportswear'),
        ('MEN\'S FASHION','Men\'s Fashion'),
        ('FASHON SALES & DEALS','Fashon Sales & Deals'),



        ('CLOTHING','Clothing'),
        ('WESTERN WEAR','Western Wear'),
        ('ETHNIC WEAR','Ethnic Wear'),
        ('LINGERIE & NIGHTWEAR','Lingerie & Nightwear'),
        ('TOP BRANDS','Top Brands'),
        ('WATCHES','Watches'),
        ('HANDBAGS & CLUTCHES','Handbags & Clutches'),
        ('GOLD & DIAMOND JEWELLERY','Gold & Diamond Jewellery'),
        ('FASHION JEWELLERY','Fashion Jewellery'),
        ('SUNGLASSES','Sunglasses'),
        ('SHOES','Shoes'),
        ('FASHION SANDALS','Fashion Sandals'),
        ('BALLERINAS','Ballerinas'),
        ('HANDLOOMS & HANDICRAFTS STORE','Handlooms & Handicrafts Store'),
        ('SPORTSWEAR','Sportswear'),
        ('WOMEN\'S FASHION','Women\'s Fashion'),
        ('FASHON SALES & DEALS','Fashon Sales & Deals'),



        ('KITCHEN & DINING','Kitchen & Dining'),
        ('KITCHEN STORAGE & CONTAINERS','Kitchen Storage & Containers'),
        ('FURNITURE','Furniture'),
        ('HOME FURNISHING','Home Furnishing'),
        ('BEDROOM LINEN','Bedroom Linen'),
        ('HOME DÉCOR','Home Décor'),
        ('GARDEN & OUTDOORS','Garden & Outdoors'),
        ('HOME STORAGE','Home Storage'),
        ('INDOOR LIGHTING','Indoor Lighting'),
        ('HOME IMPROVEMENT','Home Improvement'),
        ('SEWING & CRAFT SUPPLIES','Sewing & Craft Supplies'),
        ('ALL HOME & KITCHEN','All Home & Kitchen'),
        ('SHOP BY ROOM','Shop by Room'),
        ('HOME & KITCHEN DEALS','Home & Kitchen Deals'),
        ('ALL PET SUPPLIES','All Pet Supplies'),
        ('DOGS','Dogs'),



        ('BEAUTY & GROOMING','Beauty & Grooming'),
        ('LUXURY BEAUTY','Luxury Beauty'),
        ('MAKE-UP','Make-up'),
        ('HEALTH & PERSONAL CARE','Health & Personal Care'),
        ('HOUSEHOLD SUPPLIES','Household Supplies'),
        ('PERSONAL CARE APPLIANCES','Personal Care Appliances'),
        ('VALUE BAZAAR','Value Bazaar'),
        ('ALL GROCERY & GOURMET FOODS','All Grocery & Gourmet Foods'),
        ('COFFEE, TEA & BEVERAGES','Coffee, Tea & Beverages'),
        ('SNACK FOODS','Snack Foods'),



        ('CRICKET','Cricket'),
        ('BADMINTON','Badminton'),
        ('CYCLING','Cycling'),
        ('FOOTBALL','Football'),
        ('RUNNING','Running'),
        ('CAMPING & HIKING','Camping & Hiking'),
        ('FITNESS ACCESSORIES','Fitness Accessories'),
        ('YOGA','Yoga'),
        ('STRENGTH TRAINING','Strength Training'),
        ('CARDIO EQUIPMENT','Cardio Equipment'),
        ('ALL EXERCISE & FITNESS','All Exercise & Fitness'),
        ('ALL SPORTS, FITNESS & OUTDOORS','All Sports, Fitness & Outdoors'),
        ('BAGS & BACKPACKS','Bags & Backpacks'),
        ('CABIN BAGS','Cabin Bags'),
        ('CHECK-IN BAGS','Check-in Bags'),
        ('TRAVEL DUFFLES','Travel Duffles'),
        ('TRAVEL ACCESSORIES','Travel Accessories'),
        ('WALLETS','Wallets'),



        ('TOYS & GAMES','Toys & Games'),
        ('BABY PRODUCTS','Baby Products'),
        ('DIAPERS','Diapers'),
        ('BABY WISH LIST','Baby Wish List'),
        ('TOYS GIFTING STORE','Toys Gifting Store'),
        ('STEM TOYS STORE','STEM Toys Store'),
        ('INTERNATIONAL TOY STORE','International Toy Store'),
        ('BABY BATH, SKIN & GROOMING','Baby Bath, Skin & Grooming'),
        ('STROLLERS & PRAMS','Strollers & Prams'),
        ('NURSING & FEEDING','Nursing & Feeding'),




        ('KIDS\' CLOTHING','Kids\' Clothing'),
        ('KIDS\' SHOES','Kids\' Shoes'),
        ('SCHOOL BAGS','School Bags'),
        ('KIDS\' WATCHES','Kids\' Watches'),
        ('KIDS\' FASHION','Kids\' Fashion'),
        ('BABY FASHION','Baby Fashion'),



        ('MOTORBIKE ACCESSORIES & PARTS','Motorbike Accessories & Parts'),
        ('CAR ACCESSORIES','Car Accessories'),
        ('CAR ELECTRONICS','Car Electronics'),
        ('CAR PARTS','Car Parts'),
        ('CAR & BIKE CARE','Car & Bike Care'),
        ('ALL CAR & MOTORBIKE PRODUCTS','All Car & Motorbike Products'),
        ('INDUSTRIAL & SCIENTIFIC SUPPLIES','Industrial & Scientific Supplies'),
        ('TEST, MEASURE & INSPECT','Test, Measure & Inspect'),
        ('LAB & SCIENTIFIC','Lab & Scientific'),
        ('JANITORIAL & SANITATION SUPPLIES','Janitorial & Sanitation Supplies'),
        ('ALL BOOKS','All Books'),
        ('FICTION BOOKS','Fiction Books'),
        ('EDITOR\'S CORNER','Editor\'s Corner'),
        ('SCHOOL TEXTBOOKS','School Textbooks'),
        ('CHILDREN\'S BOOKS','Children \'s Books'),
        ('EXAM CENTRAL','Exam Central'),
        ('TEXTBOOKS','Textbooks'),
        ('INDIAN LANGUAGE BOOKS','Indian Language Books'),
        ('USED BOOKS','Used Books'),




        ('ALL MOVIES & TV SHOWS','All Movies & TV Shows'),
        ('BLU-RAY','Blu-ray'),
        ('ALL ENGLISH','All English'),
        ('ALL HINDI','All Hindi'),
        ('GAMING CONSOLES','Gaming Consoles'),
        ('LATEST VIDEO GAMES','Latest Video Games'),
        ('GAMING ACCESSORIES','Gaming Accessories'),
        (' PC GAMES ',' PC Games '),
        ('VIDEO GAMES DEALS','Video Games Deals'),
        ('ALL VIDEO GAMES','All Video Games'),
        ('ALL MUSIC','All Music'),
        ('INTERNATIONAL MUSIC','International Music'),
        ('FILM SONGS','Film Songs'),
        ('INDIAN CLASSICAL','Indian Classical'),
        ('MUSICAL INSTRUMENTS & PROFESSIONAL AUDIO','Musical Instruments & Professional Audio'),



        (' ALL GIFT CARDS',' All Gift Cards'),
        ('POPULAR GIFT CARDS','Popular Gift Cards'),
        ('GIFT BOXES, GIFT TAGS, GREETING CARDS','Gift Boxes, Gift Tags, Greeting Cards'),
        ('POPULAR BRAND GIFT VOUCHERS ','Popular Brand Gift Vouchers '),
        ('BIRTHDAY GIFT CARDS','Birthday Gift Cards'),
        ('WEDDING & ANNIVERSARY ','Wedding & Anniversary '),
        ('BEST WISHES & THANK YOU','Best Wishes & Thank You'),
        ('CORPORATE GIFT CARDS','Corporate Gift Cards'),
        ('ADD A GIFT CARD','Add a gift card'),



        ('CLOTHING & ACCESSORIES','Clothing & Accessories'),
        ('WATCHES','Watches'),
        ('HOME & KITCHEN','Home & Kitchen'),
        ('SHOES','Shoes'),
        ('PC & ELECTRONICS','PC & Electronics'),
        ('OFFICE SUPPLIES','Office Supplies'),
        ('SPORTS & FITNESS','Sports & Fitness'),
        ('BOOKS','Books'),
        ('GLOBAL STORE','Global Store'),





    )
    catagory = models.ForeignKey(ProductCatagory)
    subcatagory = models.CharField(choices=PRODUCT_SUBCATAGORY_LIST, max_length=254, blank= True, unique=True)
    other_subcatagory = models.CharField(max_length=254, blank=True)

    def __str__(self):
        if (self.subcatagory):
            return str(self.subcatagory)
        else:
            return str(self.other_subcatagory)


class Product(models.Model):

    product_subcatagory = models.ForeignKey(ProductSubcatagory)
    seller = models.ForeignKey(Seller, default=1)

    product_id = models.CharField(max_length=50, unique=True)
    brand = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    mrp = models.IntegerField()
    price = models.IntegerField()
    # discount_regex = RegexValidator(regex=r'^[1-9][0-9]?$|^100$',)
    discount = models.IntegerField()
    # in_stock = models.BooleanField()
    # color = models.CharField(max_length=10)
    # quantity = models.IntegerField()
    # weight = models.IntegerField()
    # length = models.IntegerField()
    # hight = models.IntegerField()
    # SKU = models.CharField(max_length=50)
    short_desc = models.TextField()
    full_desc = models.TextField()
    image = models.ImageField()

    def __str__(self):
        return str(self.name)

class Order(models.Model):
    Order_id = models.CharField(max_length=50,)
    seller = models.ForeignKey(Seller)
    buyer = models.ForeignKey(Buyer)
    product = models.ForeignKey(Product)
    total_cost = models.IntegerField(default=0)
    shipping_address = models.TextField()
    city = models.CharField(max_length=254)
    pin_code = models.CharField(max_length=254)
    payment_status = models.CharField(max_length=50)
    order_status = models.CharField(max_length=50)
    payment_mode = models.CharField(max_length=50)




class AllMobilePhoneSpecification(models.Model):
    product = models.OneToOneField(Product)
    OS = models.CharField(max_length=50, blank=True)
    RAM = models.CharField(max_length=50, blank=True)
    Item_Weight = models.CharField(max_length=50, blank=True)
    Wireless_communication_technologies = models.CharField(max_length=254 )
    Connectivity_technologies = models.CharField(max_length=254)
    Special_features = models.TextField()
    Camera_features = models.CharField(max_length=254)
    Form_factor = models.CharField(max_length=251)

    Colour = models.CharField(max_length=50)
    Battery_Power_Rating = models.CharField(max_length=10)
    Phone_Talk_Time = models.CharField(max_length=10)
    Phone_Standby_time = models.CharField(max_length=10)
    Whats_in_the_box = models.TextField()
    Avilable = models.IntegerField(default=0)


















