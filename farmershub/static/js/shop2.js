

let menu = document.querySelector("#menu-bar");
let navbar = document.querySelector(".navbar");
let header = document.querySelector(".header-2");

menu.addEventListener("click", () => {
  menu.classList.toggle("fa-times");
  navbar.classList.toggle("active");
});
window.onscroll = () => {
  menu.classList.remove("fa-times");
  navbar.classList.remove("active");

  if (window.screenY > 150) {
    header.classList.add("active");
  } else {
    header.classList.remove("active");
  }
};

// function addToCart(id, price,name) {
//   console.log(" Product Id :", id);
//   console.log(' Price ', price);

//   let quantity = document.getElementById('quantity').value
//   console.log('quantity:', quantity);

//   var cartData = JSON.parse(localStorage.getItem('cart')) || [];

//   let Item = {
//     UserId: "",
//     productId: id,
//     productPrice: price,
//     quantity,
//     productName:name
//   }

//   cartData.push(Item)

//   localStorage.setItem('cart', JSON.stringify(cartData));
//   var retrievedCartData = JSON.parse(localStorage.getItem("cart"));
//   console.log(retrievedCartData);
// } 
function addToCart(id, price, name) {
  console.log(" Product Id :", id);
  console.log(' Price ', price);

  let quantity = document.getElementById('quantity').value;
  console.log('quantity:', quantity);

  var cartData = JSON.parse(localStorage.getItem('cart')) || [];

  // Check if the item with the same productId already exists in the cart
  let existingItem = cartData.find(item => item.productId === id);

  if (existingItem) {
    // Item already exists, update the quantity
    existingItem.quantity = parseInt(existingItem.quantity) + parseInt(quantity);
  } else {
    // Item doesn't exist, add it to the cart
    let item = {
      UserId: "",
      productId: id,
      productPrice: price,
      quantity: quantity,
      productName: name
    };

    cartData.push(item);
  }

  localStorage.setItem('cart', JSON.stringify(cartData));
  var retrievedCartData = JSON.parse(localStorage.getItem("cart"));
  console.log(retrievedCartData);
}








