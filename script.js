
main = document.getElementById('infos')

function Verificapol () {
    let opcoes = document.getElementsByName('pol')
    let polarizacao = null  

    for (let c = 0; c < opcoes.length; c++){
        if (opcoes[c].checked){
            polarizacao = opcoes[c].value;
            break;
        }
    }

    if (polarizacao == "dtg"){
        
    }
}

