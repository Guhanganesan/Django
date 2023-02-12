# SETUP SSH IN LOCAL MACHINE
1. git clone git@github.com:Guhanganesan/Django.git      <=>
2. ssh-keygen -t ed25519 -C "example@email.com"     <=>
3. eval "$(ssh-agent -s)"       <=>  
4. ssh-add ~/.ssh/id_ed25519       <=>
5. clip < ~/.ssh/id_ed25519.pub (copy it to add your ssh account)       <=> 
6. Visit https://github.com/settings/keys (add new ssh key after copied step 5)         <=> 
7. git clone git@github.com:Guhanganesan/Django.git 

