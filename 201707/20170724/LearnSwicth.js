/**
 * Created by JianJian on 2017/7/25.
 */

var a = "HelloWorld";

switch (a){
    case 1:
        /* merge */
    case 2:
        console.log(a);
        break;
    case 5:
        console.log(a+3);
        break;
    case "Hello"+"World":
        console.log(a+"!!!");
        break;
    default:
        console.log("Yeah!");
}

