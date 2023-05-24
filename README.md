# ApiX - Final Beta (Release Version)
<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>

The code it's not finished, validation in progress.

### Disclaimer

This code was provide for free usage, file manipulation and more security, its **forbidden to sell the code, sell programs that include the library or exploid data from other people.**

**Its needed to be the github source code link** in every update from the community in their repository.

The commercial use is **only for the company inside system**.

## About 

### What APIX stands ? 

It's was supposed to be a better version for API Keys, but i like the name **ApiXtreme** so i use it anyways.

### How can i use it ?

Just download the template, use it freely, and make the world more secure.

### Can i modify ?

You can modify the program and make it more efficient, secure and improved.

### I downloaded but i don't know how to start !

You need to provide the library two files with differente extensions :
- `encripted-content.apix`
- `source-for-encrypt.apixi`

After having these two file you need to put the files on this way :
- `/api/encripted-content.apix`
- `/encode/source-for-encrypt.apixi`

**The library read the file in that specific directory so this should be in this way :**
```
|-- your-project
|   |-- project.py
|   |-- libraries
|   |   |-- apix.py
|   |   |   |-- encode
|   |   |   |   |-- source-for-encrypt.apixi
|   |   |   |-- api
|   |   |   |   |-- encripted-content.apix
```

You will need to start your code by doing :

```
from library.apix import ApiXInterpreter as Apix
```

Then you can use it freely like in **index.py**.

### Why you use the extensions `.apix` and `.apixi` ?

`.apixi` is for the file that provides the encrypted caracters, this extention symbolizes `.apixtremeinterpreter`.

`.apix` is for the file that has the encrypted content, this extention symbolizes `.apixtreme`.

## Built With
Python

## Future Versions in
Javascript

## License

Distributed under the MIT License. 

**Read the disclaimer before using it**
