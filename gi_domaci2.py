import pysam 

numUnmappedReads = 0;
numAllrds = 0;
numMappingZero = 0;
mappingQuality = 0;

file = pysam.AlignmentFile("merged-tumor.bam", "rb");

for rd in file.fetch(until_eof=True):
    mappingQuality += rd.mapping_quality;
    numAllrds += 1;
    
    if rd.is_unmapped: 
        numUnmappedReads += 1;
    if rd.mapping_quality == 0:
        numMappingZero += 1;
    
file.close()

print("Number of unmapped reads: " + str(numUnmappedReads));
print("Total number of reads: " + str(numAllrds));
print("Number of reads with mapping quality 0: " + str(numMappingZero));
print("Average mapping quality for all the reads: " + str(mappingQuality / numAllrds));
print("Average mapping quality if reads with 0 mapp quality are filtered out: " + str(mappingQuality / (numAllrds - numMappingZero)));

