buttons.forEach((button) => {
    button.addEventListener('click', function(){
        if(!tg.MainButton.isVisible){
            generalCart++;

            item = this.parentElement.parentElement.querySelector('.count').dataset.item_id;
            let img_src =  this.parentElement.parentElement.querySelector('.img_menu').src
            let price = this.parentElement.parentElement.querySelector('.button_card').innerHTML;
            let price_number = price.split(' ')[0];
            let currencyId = price.split(' ')[1];

            let choose_div = document.getElementById('name_'+item)
            itemsNamesInCart.push(choose_div.innerHTML);

            let count = document.getElementById('in_cart_'+item).value;
            let replacement = itemsNamesCountInCart.find(obj => obj.name === choose_div.innerHTML)
            if (replacement){
                replacement.count = count;
            }
            else{
                itemsNamesCountInCart.push({name: choose_div.innerHTML, picture: img_src, price: price_number, currencyId: currencyId, id: item,count: count})
                console.log('123')
                console.log({name: choose_div.innerHTML, picture: img_src, price: price_number, currencyId: currencyId, id: item,count: count})
            }
            item_count1 = document.getElementById('in_cart').innerHTML;
            tg.MainButton.setText("Переглянути замовлення ("+generalCart+")");
        }
        else{
            generalCart++;
            item = this.parentElement.parentElement.querySelector('.count').dataset.item_id;

            let img_src =  this.parentElement.parentElement.querySelector('.img_menu').src
            let price = this.parentElement.parentElement.querySelector('.button_card').innerHTML;
            let price_number = price.split(' ')[0];
            let currencyId = price.split(' ')[1];

            let choose_div = document.getElementById('name_'+item)
            itemsNamesInCart.push(choose_div.innerHTML);
            let count = document.getElementById('in_cart_'+item).value;
            let replacement = itemsNamesCountInCart.find(obj => obj.name === choose_div.innerHTML)
            if (replacement){
                replacement.count = count;
            }
            else{
                itemsNamesCountInCart.push({name: choose_div.innerHTML, picture: img_src, price: price_number, currencyId: currencyId, id: item,count: count})
                console.log('123')
                console.log({name: choose_div.innerHTML, picture: img_src, price: price_number, currencyId: currencyId, id: item,count: count})
            }
            
            console.log(itemsNamesCountInCart)
            item_count1 = document.getElementById('in_cart').innerHTML;

            btn_container.innerHTML =`<button type="submit" class="btn_to_cart" onclick= "to_cart({{novaPost}})">Переглянути замовлення (${generalCart})</button>` 
            tg.MainButton.setText("Переглянути замовлення ("+generalCart+")");
        }
        localStorage.setItem('generalCartCount', generalCart);
        itemsNamesInCartJson = JSON.stringify(itemsNamesInCart)
        localStorage.setItem('itemsNamesInCart', itemsNamesInCartJson);
        itemsNamesCountInCartJson = JSON.stringify(itemsNamesCountInCart)
        localStorage.setItem('itemsNamesCountInCart', itemsNamesCountInCartJson);
    });
  });
buttons1.forEach((button) => {
    button.addEventListener('click', function(){
        if(!tg.MainButton.isVisible){
            generalCart--;
            item = this.parentElement.parentElement.querySelector('.count').dataset.item_id;
            let choose_div = document.getElementById('name_'+item)
            itemsNamesInCart.pop();
            let replacement = itemsNamesCountInCart.find(obj => obj.name === choose_div.innerHTML)
            if (replacement){
                replacement.count--;
            }
            item_count1 = document.getElementById('in_cart').innerHTML;
            btn_container.innerHTML =`<button type="submit" class="btn_to_cart" onclick= "to_cart({{novaPost}})">Переглянути замовлення (${generalCart})</button>`
        }
        else{
            generalCart--;
            item = this.parentElement.parentElement.querySelector('.count').dataset.item_id;
            let choose_div = document.getElementById('name_'+item)
            itemsNamesInCart.pop();
            let replacement = itemsNamesCountInCart.find(obj => obj.name === choose_div.innerHTML)
            if (replacement){
                replacement.count--;
            }
            item_count1 = document.getElementById('in_cart').innerHTML;
            btn_container.innerHTML =`<button type="submit" class="btn_to_cart" onclick= "to_cart({{novaPost}})">Переглянути замовлення (${generalCart})</button>`
        }
        localStorage.setItem('generalCartCount', generalCart);
        itemsNamesInCartJson = JSON.stringify(itemsNamesInCart)
        localStorage.setItem('itemsNamesInCart', itemsNamesInCartJson);
        itemsNamesCountInCartJson = JSON.stringify(itemsNamesCountInCart)
        localStorage.setItem('itemsNamesCountInCart', itemsNamesCountInCartJson);
    });
  });
buttons2.forEach((button) => {
    button.addEventListener('click', function(){
        if(!tg.MainButton.isVisible){
            generalCart++;
            item = this.parentElement.parentElement.querySelector('.count').dataset.item_id;

            let img_src =  this.parentElement.parentElement.querySelector('.img_menu').src
            let price = this.parentElement.parentElement.querySelector('.button_card').innerHTML;
            let price_number = price.split(' ')[0];
            let currencyId = price.split(' ')[1];

            let choose_div = document.getElementById('name_'+item)
            itemsNamesInCart.push(choose_div.innerHTML);
            let count = document.getElementById('in_cart_'+item).value;
            let replacement = itemsNamesCountInCart.find(obj => obj.name === choose_div.innerHTML)
            if (replacement){
                replacement.count = count;
            }
            else{
                itemsNamesCountInCart.push({name: choose_div.innerHTML, picture: img_src, price: price_number, currencyId: currencyId, id: item,count: count})
            }
            item_count1 = document.getElementById('in_cart').innerHTML;
            btn_container.innerHTML =`<button type="submit" class="btn_to_cart" onclick= "to_cart({{novaPost}})">Переглянути замовлення (${generalCart})</button>`
        }
        else{
            generalCart++;
            item = this.parentElement.parentElement.querySelector('.count').dataset.item_id;

            let img_src =  this.parentElement.parentElement.querySelector('.img_menu').src
            let price = this.parentElement.parentElement.querySelector('.button_card').innerHTML;
            let price_number = price.split(' ')[0];
            let currencyId = price.split(' ')[1];

            let choose_div = document.getElementById('name_'+item)
            itemsNamesInCart.push(choose_div.innerHTML);
            let count = document.getElementById('in_cart_'+item).value;
            let replacement = itemsNamesCountInCart.find(obj => obj.name === choose_div.innerHTML)
            if (replacement){
                replacement.count = count;
            }
            else{
                itemsNamesCountInCart.push({name: choose_div.innerHTML, picture: img_src, price: price_number, currencyId: currencyId, id: item,count: count})
            }
            item_count1 = document.getElementById('in_cart').innerHTML;
            tbtn_container.innerHTML =`<button type="submit" class="btn_to_cart" onclick= "to_cart({{novaPost}})">Переглянути замовлення (${generalCart})</button>`
        }
        localStorage.setItem('generalCartCount', generalCart);
        itemsNamesInCartJson = JSON.stringify(itemsNamesInCart)
        localStorage.setItem('itemsNamesInCart', itemsNamesInCartJson);
        itemsNamesCountInCartJson = JSON.stringify(itemsNamesCountInCart)
        localStorage.setItem('itemsNamesCountInCart', itemsNamesCountInCartJson);
    });
  });
  
  tg.onEvent("mainButtonClicked", function (){
    let itemsNamesCountInCartJson = localStorage.getItem('itemsNamesCountInCart')
    let itemsNamesCountInCart = JSON.parse(itemsNamesCountInCartJson);
    let s = "";
    let i = 0;
    let cid = ""
    itemsNamesCountInCart.forEach(item=>{
        if(item.count != 0){
            s=s+item.name+" - "+ item.count + " шт.\n";
            i = i + parseInt(item.price)*parseInt(item.count);
            cid = item.currencyId
        }

    })
    let res = s + "\n На суму "+ i + cid
    let offer = s;
    let price = i;
    let result = {'message': res, 'offer': offer, 'amount': price}
    tg.sendData(result);
    localStorage.clear();
});