require(ggplot2)
install.packages("viridis")
library(viridis)

#Set your working directory to the Analysis folder for your project

#Read in the data
initial_data <- read.table("6-23-25_stress_death_chance_repeat/munged_basic.dat", h=T)
final_update <- subset(initial_data, update == "1000")

#Plot the host and symbiont interaction values by vertical transmission rate
ggplot(data=final_update, aes(x=partner, y=donate, color=partner)) + geom_boxplot(alpha=0.5, outlier.size=0) + ylab("Final Interaction Value") + xlab("Partner") + theme(panel.background = element_rect(fill='white', colour='black')) + theme(panel.grid.major = element_blank(), panel.grid.minor = element_blank()) + guides(fill=FALSE) +ylim(-1,1) + scale_color_manual(name="Vertical Transmission\nRate", values=viridis(2)) + facet_wrap(~treatment)
