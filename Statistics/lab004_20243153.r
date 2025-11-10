data = read.table("data.txt")
data = data.frame(lapply(data, function(x) if (is.numeric(x)) round(x, 3) else x))

print(nrow(data))
print(data[10, ])

model <- lm(V2 ~ V1, data = data)
alpha = round(unname(coef(model)[1]),3)
beta = round(unname(coef(model)[2]),3)
print(alpha)
print(beta)

t_value =  summary(model)$coefficients[2, "t value"]
print(t_value)

r_squared = round(summary(model)$r.squared,3)
print(r_squared)

v1_10 <- data$V1[10]
conf_int <- predict(model, newdata = data.frame(V1 = v1_10), interval = "confidence", level = 0.95)
print(conf_int)

pred_int <- predict(model, newdata = data.frame(V1 = v1_10), interval = "prediction", level = 0.95)
print(pred_int)

standardized_residuals <- rstandard(model)
bmp("res.bmp")
plot(data$V1, standardized_residuals,
     ylab = "Standardized Residual",
     xlab = "V1",
     main = "Standardized Residuals")
dev.off()
