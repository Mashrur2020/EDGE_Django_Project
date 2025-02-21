from django.shortcuts import render

# Home Page View
def home(request):
    return render(request, 'index.html')

# Watch Store - Blog Page View
def watch_list(request):
    posts = [
        {
            "id": 1,
            "title": "Luxury Watches for Collectors",
            "description": "Explore the most prestigious Rolex watches, perfect for collectors and enthusiasts.",
            "image": "https://wristadvisor.com/wp-content/uploads/2023/01/Luxury-Watches-The-Top-Luxury-Watch-Brands-1024x512.jpg",
            "buy_url": "https://www.amazon.com/Breitling-Chronoliner-Automatic-Chronograph-BE83-761P/dp/B07DKTRGR8/ref=sr_1_10?dib=eyJ2IjoiMSJ9._RSVwRuXX2RwZIKoZ6X2QBjDIK-JJ9Cns1ncXOKjyQReuZ7gK6hEGV52mM6E7AL9M5qH33pKECzYAByFrujVLdBzePmSbPtiVxEOUi-hnAsr5qq8pYwsllxGvU8xM4YoNt1OuiF0hDF8X9Ij3U7BaOpWI48TMqbqQS9DAmn7CDQkd0mGN4sQz8zB1MmnURsBDE1j0BzeimH-pYJ_M1RB7N9XYL_XdUbUjId0rQk2oV4mEH_GU8N_XBBwEZdi3vUVaIPuaiJbY0HCjJ-bwiJR1Q.jFYoxRIKcRW8DxRkozUTICIcWtxe5L5NosYyu0XW4A0&dib_tag=se&qid=1740081771&refinements=p_36%3A2690000-%2Cp_n_feature_nine_browse-bin%3A5021361011&rnid=2661611011&s=apparel&sr=1-10",
            "brand": "Rolex",
            "price": 12500.00
        },
        {
            "id": 2,
            "title": "Best Smartwatches for Fitness and Work",
            "description": "Stay connected and track your health with the latest smartwatches.",
            "image": "https://www.uniformwares.com/wp-content/uploads/2021/07/best-apple-watch-alternatives.png",
            "buy_url": "https://www.uniformwares.com/apple-watch-alternatives/",
            "brand": "Apple Watch",
            "price": 399.99
        },
        {
            "id": 3,
            "title": "Timeless Classic Leather Watches",
            "description": "Discover elegant leather strap watches for a sophisticated look.",
            "image": "https://watchdirect.shop/cdn/shop/files/ES5297-3P-1_1000x.jpg?v=1718770777",
            "buy_url": "https://watchdirect.shop/products/fossil-carlie-three-hand-medium-brown-leather-watch-es5297",
            "brand": "Fossil",
            "price": 159.99
        },
    ]
    return render(request, 'blog.html', {'posts': posts})


    return render(request, 'blog.html', {'posts': posts})
