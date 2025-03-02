
export const toggle = (coin: Ref<number>) => () => coin.value = ++coin.value % 2;

export const useToggleParam = () => 
{
  const coin = useState('coin', () => (0));

  return { coin: readonly(coin), toggle: toggle(coin) };
}
