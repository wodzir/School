# sadasfsa
install.packages("stringr")
#nejvíc užitečná knihovna (tidyverse), je jich tam víc
install.packages("tidyverse") 
library(tidyverse)
str_trim("    ahoj svete   ")


y <- 2:10
y <- seq(2, 10, 2)
y[3]
y[-1]

f <- function(x){return(x^3)}
f(3)


for (i in 1:10) print (i)
plot (iris$Sepal.Length, iris$Sepal.Width) 
plot(sin)

TRUE && TRUE 
TRUE && FALSE  

4 %% 2 == 0 && 6 %% 2 == 0 

x <- 1:10
y <- rep(1,10)

rep(x,2)
rep(x,2, each=2)
x==y

A <- matrix(1:9, nrow=3)
B <- matrix(1:9, nrow=3, byrow=TRUE)

vektor1 <- c(1,2,3)
vektor2 <- c(3,4,5)
print(vektor1+vektor2)

sum(vektor1*vektor2)

names(vektor1) <- c("a", "b", "c")

#zapoctak, z cviceni prezencaku 
library(readr)
shootings <- read_csv("C:/Users/mvode/OneDrive/Desktop/Rko/shootings.csv")
View(shootings)




