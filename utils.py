def clean_my_list(my_list):
    '''
        Puhastab antud nimekirja elementide alhusest ja lõpust tühikud ning reavahetehused

        Args:
            some_list (list): Nimekiri, mis sisaldab puhastamata tekstielemente (nt faili read koos \n märgiga)

        Returns:
            list: Uus nimekiri, kus kõik elemendid on puhastatud liigsetest tühikutest ja reavahetustest

    '''
    
    clean_list = []

    for element in my_list:
        clean_element = element.strip()
        clean_list.append(clean_element)

    return clean_list
