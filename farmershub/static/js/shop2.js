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





let countDate = new Date('june1, 2022, 00:00:00').getTime();
function CountDown(){
  let now=new Date().getTime();
  gap=countDate-now;
  let second=1000;
  let minute=second*60;
  let hour=minute*60
  let day=hour*24

}