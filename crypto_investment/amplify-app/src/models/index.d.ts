import { ModelInit, MutableModel, __modelMeta__, ManagedIdentifier } from "@aws-amplify/datastore";
// @ts-ignore
import { LazyLoading, LazyLoadingDisabled } from "@aws-amplify/datastore";





type EagerCryptoPrice = {
  readonly [__modelMeta__]: {
    identifier: ManagedIdentifier<CryptoPrice, 'id'>;
    readOnlyFields: 'createdAt' | 'updatedAt';
  };
  readonly id: string;
  readonly Date?: string | null;
  readonly Coin?: string | null;
  readonly Price?: number | null;
  readonly createdAt?: string | null;
  readonly updatedAt?: string | null;
}

type LazyCryptoPrice = {
  readonly [__modelMeta__]: {
    identifier: ManagedIdentifier<CryptoPrice, 'id'>;
    readOnlyFields: 'createdAt' | 'updatedAt';
  };
  readonly id: string;
  readonly Date?: string | null;
  readonly Coin?: string | null;
  readonly Price?: number | null;
  readonly createdAt?: string | null;
  readonly updatedAt?: string | null;
}

export declare type CryptoPrice = LazyLoading extends LazyLoadingDisabled ? EagerCryptoPrice : LazyCryptoPrice

export declare const CryptoPrice: (new (init: ModelInit<CryptoPrice>) => CryptoPrice) & {
  copyOf(source: CryptoPrice, mutator: (draft: MutableModel<CryptoPrice>) => MutableModel<CryptoPrice> | void): CryptoPrice;
}