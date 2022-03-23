import matplotlib.pyplot as plt
import numpy as np

######################
###Enter data here: ##
######################

#data was copied in from terminal output
svm_accuracy = ([0.8505338078291815, 0.5724381625441696, 0.8095238095238095, 0.6271929824561403, 0.6485507246376812, 0.5116279069767442, 0.8628158844765343, 0.8708487084870848, 0.8560606060606061])
knn_accuracy = ([0.8185053380782918, 0.5618374558303887, 0.7875457875457875, 0.5789473684210527, 0.6159420289855072, 0.46511627906976744, 0.7364620938628159, 0.7970479704797048, 0.8181818181818182])
lda_accuracy = ([0.8434163701067615, 0.5759717314487632, 0.8021978021978022, 0.6535087719298246, 0.36231884057971014, 0.4604651162790698, 0.9133574007220217, 0.8523985239852399, 0.7613636363636364])

svm_avg_accuracy = 0.7343991769991056
knn_avg_accuracy = 0.6866206822727927
lda_avg_accuracy = 0.691666465956981

######################
######################
######################

######################
###Creating plot: ####
######################

#x axis
num_dataset = np.array([1,2,3,4,5,6,7,8,9,"average"])

#y axis (add in the avg_accuracy metrics, multiply everything by 100 to convert from decimal to %)
svm_accuracy.append(svm_avg_accuracy)
knn_accuracy.append(knn_avg_accuracy)
lda_accuracy.append(lda_avg_accuracy)

svm_accuracy = [element * 100 for element in svm_accuracy]
knn_accuracy = [element * 100 for element in knn_accuracy]
lda_accuracy = [element * 100 for element in lda_accuracy]

#datapoints
plt.plot(num_dataset, svm_accuracy, 'o')
plt.plot(num_dataset, knn_accuracy, 'o')
plt.plot(num_dataset, lda_accuracy, 'o')

#key
plt.legend(["SVM", "KNN", "LDA"])

#axis labels
plt.xlabel("Subset Number (1-9) of Dataset")
plt.ylabel("Accuracy Rate (%)")

#display the plot
plt.show()
