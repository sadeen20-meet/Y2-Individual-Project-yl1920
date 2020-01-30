from model import Base, User, Product


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,scoped_session


engine = create_engine('sqlite:///database.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = scoped_session(sessionmaker(bind=engine,autoflush=False))
 
def save_to_database(f,l,e,p):
	user = User(
		firstname=f,
		lastname=l,
		email=e,
		password=p)
	session.add(user)
	session.commit()

def queryAllUsers():
	return session.query(User).all()

def check(e,p):
	user=session.query(User).filter_by(email=e).first()
	if user != None:
		if user.password == p :
			c = True
		else:
			c = False
		return c
	else:
		return False

print(check('h@m',"secret"))
print(queryAllUsers() )

def add_product(name,price,description,picture_link):
	product_object = Product(
	
	name=name,
	price=price,
	description=description,
	picture_link=picture_link)
	session.add(product_object)
	session.commit()

# add_product("cukur T-shirt","12$","Cukur sign","https://ih0.redbubble.net/image.691285991.9156/ra,unisex_tshirt,x3104,black,front-c,700,650,750,900-bg,ffffff.jpg")
# add_product("cukur shirt","12$","If there isn't a problem that means that there is","https://www.artistshot.com/assets-3/images/admin/product_design/7227381/s-k-nt-yoksa-s-k-nt-var-demektir-ukur-for-light-long-sleeve-shirts.jpg")
# add_product("cukur sweater","20$","cukur sign sweater","https://images.cloudpuble.com/thumb/1010x1010/27.front/Black.0/a32c1e4c7beebe859063184027cafc2c/a7/2019/05/20/VBkN-5ce2e7a5a949d.png")
# add_product("cukur hoodie","25$","cukur sign hoodie","https://www.zepplingiyim.com/10487-large_default/cukur-logo-1-kapsonlu-sweatshirt-hoodie.jpg")
# add_product("cukur jacket","30$","cukur bomber jacket","https://lookadikoy-img.ticimaxcdn.com/Uploads/UrunResimleri/buyuk/Cukur-Bomber-Ceket-8d94.png")
# add_product("cukur baby shirt","10$","cukur tiny shirt","https://res.cloudinary.com/teepublic/image/private/s--pZpL_V5X--/t_Resized%20Artwork/c_crop,x_10,y_10/c_fit,w_292/c_crop,g_north_west,h_389,w_292,x_0,y_-16/g_north_west,u_upload:v1457730363:production:blanks:sixjuikxrsgkogzk0hc7,x_-495,y_-323/b_rgb:eeeeee/c_limit,f_jpg,h_630,q_90,w_630/v1553190575/production/designs/4464538_0.jpg")
def query_all():

   products = session.query(Product).all()
   return products
print(query_all())

# def add_to_cart(Id):
# 	# cartproducte_object=Cart()
# 	cartproduct = Cart(productID = Id)
# 	session.add(cartproduct)

# 	session.commit()

# def query_cart_products():

#    products = session.query(Cart).all()
#    return products
# print(query_cart_products())
# add_to_cart(1)
# print(query_cart_products())