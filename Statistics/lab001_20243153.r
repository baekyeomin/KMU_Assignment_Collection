data <- read.table("data.txt")
print(nrow(data))
print(ncol(data))
condition_rows <- data[data[,2]>=1.05*data[,3],]
print(nrow(condition_rows))
second_rows <- data[data[,1]=="2024.09.11",]
print(second_rows[,2])
