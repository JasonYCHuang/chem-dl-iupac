# download the smi_to_iupac model
URL="https://bwsyncandshare.kit.edu/s/bRWQ4Y8bZmWnBEt/download"
GZ="./chem_iupac/download"

if [ -d "./chem_iupac/download" ]; then
    echo "Dataset has already been downloaded."
else
    wget "$URL" -P "./chem_iupac/"

    if [ -f $GZ ]; then
        echo "Dataset successfully downloaded."
    else
        echo "Dataset not successfully downloaded."
        exit
    fi
    tar zxvf $GZ -C ./chem_iupac/
fi


# download opsin
URL="https://github.com/dan2097/opsin/releases/download/2.4.0/opsin-2.4.0-jar-with-dependencies.jar"
GZ="./chem_iupac/opsin/opsin-2.4.0-jar-with-dependencies.jar"

if [ -d "./chem_iupac/opsin/opsin-2.4.0-jar-with-dependencies.jar" ]; then
    echo "Opsin has already been downloaded."
else
    wget "$URL" -P "./chem_iupac/opsin/"

    if [ -f $GZ ]; then
        echo "Opsin successfully downloaded."
    else
        echo "Opsin not successfully downloaded."
        exit
    fi
fi
