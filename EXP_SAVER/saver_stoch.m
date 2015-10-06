# -*- coding: utf-8 -*-

clear all
close all

clc

th0=0.95;
Nmax=15;
index=zeros(Nmax,1);
ratio=zeros(Nmax,1);



for N=1:Nmax
    zmax=1000*Nmax;  % max number of tries
    
    th=th0*zmax;    
    output=zeros(zmax,1);   
    
    for z=1:zmax
        
        counter=ones(N,1);     
        cont=0;
        
        I=1;       
        
        while (I~=0)
           
            i=floor((rand(1,1).*N)+1);  % choose one ball           
            cont=cont+1;           
            counter(i)=0;
          
            I = find(counter);
            
        end
        
        output(z,1)=cont;
        
    end
    
    
    [freq, X]=hist(output,max(output));
    
    c=cumsum(freq);    
    maxc=max(c);
    probs{N}=c./max(c);

    aux=find(c>th);
    
    index(N)=aux(1)+floor(X(1)-1);
    ratio(N)=aux(1)/N;
end

figure;
plot(index);

figure;
plot(ratio);

