#===EX.1
t = 12 
prob_vermelha = 5 / t 
prob_com_repos = prob_vermelha * prob_vermelha
p_sem_repos = (5 - 1) / (t - 1) 
prob_sem_repos = prob_vermelha * p_sem_repos

print(f"\nProbabilidade de tirar vermelha: {prob_vermelha:3f} ou {prob_vermelha:.2%} ")
print(f"Probabilidade de sair duas vermelhas na sequência COM reposição: {prob_com_repos:.3f} ou ({prob_com_repos:.2%}) ")
print(f"Probabilidade de sair duas vermelhas na sequência SEM reposição: {prob_sem_repos:.3f} ou ({prob_sem_repos:.2%}) ")


#===EX.2
d = 6
prob_dados = 3 / d
print(f"\nA probabilidade de sair um número maior que 3 ao lançar um dado de 6 lados é: {prob_dados} ou ({prob_dados:.2%})") # igual :.2f ou 


#===EX.3
m = 4
prob_moeda = 2 / m
print(f"\nA probabilidade de sair exatamente uma cara ao lançar duas moedas é: {prob_moeda} ou ({prob_moeda:.2%})")


#===EX.4
prob_verde = 2 / (5 - 1)
print(f"\nProbabilidade da próxima ser verde dado que a primeira foi vermelha: {prob_verde:.2f} ({prob_verde:.2%})")

