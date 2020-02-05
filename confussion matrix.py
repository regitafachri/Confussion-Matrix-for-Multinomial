#confussion matrix from multinomial case
mcm_train  = multilabel_confusion_matrix(y_train, y_train_pred, sample_weight=None, labels=[0,1,2,3,4,5,6,7], samplewise=False)
mcm_train


#CONFUSSION MATRIX FOR CLASS 0
#get value from array of confussion matrix
mcm00 = mcm_train[0,0]
mcm01 = mcm_train[0,1]


# intialise data of lists. 
data = {'not female_teenager(predict)':[mcm00[0], mcm01[0]], 'female_teenager(predict)':[mcm00[1], mcm01[1]]} 
# Create DataFrame 
df = pd.DataFrame(data, index=['not female_teenager(actual)','female_teenager(actual)']) 
df

#true positive
tp = mcm01[1] 
#true negative
tn = mcm00[0]
#false positive
fp = mcm00[1]
#false negative
fn = mcm01[0]

#calculating accuracy, sensitivity, spesificity, and precision
print('Accuracy      : {0:2.6f}'.format((tp+tn)*1./(tp+fp+tn+fn)))
print('Sensitivity   : {0:2.6f}'.format((tp)*1./(tp+fn)))
print('Spesificity   : {0:2.6f}'.format((tn)*1./(tn+fp)))
print('Precision     : {0:2.6f}'.format((tp)*1./(tp+fp)))

