# Lab 1


## Encrypt

* Fill _enc_inp.txt_ file with some data
* Run _encrypt.py_ script
* Specify shift number and direction

**Output data will be saved to _enc_out.txt_**

---

## Decrypt

* Fill _dec_inp.txt_ file with encrypted data | or simply change constant to point to _enc_out.txt_
* Run _decrypt.py_ script
* Specify shift number and direction. You have to specify same direction as while encoding (script will automatically reverse it).

**Output data will be saved to _dec_out.txt_**
___

## Frequency analysis

* Complete encryption step or fill _enc_out.txt_ file with some encrypted data
* Run _analyze.py_ script

##### Script will output
* Most common letters of encrypted text
* Encryption shift (number and direction) based on the distance between the most common letter and **e**